from habanero import Crossref
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import pandas as pd
import itertools
from pathlib import Path
import sys
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urlparse
from time import sleep


def get_journal_info(journal_name):
    cr = Crossref()
    journal = cr.journals(query=journal_name)
    return journal

def get_paper_by_keyword(keyword):
    cr = Crossref()
    papers = cr.works(query=keyword)
    return papers

def get_papers(journal_list="available_journals.csv"):
    df = pd.read_csv(journal_list, index_col=0)
    df = df.dropna()
    df = df.reset_index()
    
    # print(df)

    for i in range(200, len(df)):
        # i = 101
        journal_title = df["Title"][i]
        expected_papers = df["Number of papers since 2010"][i]
        issn = df["ISSN"][i]
        issn = issn.replace("'", "")
        issn = issn.replace("[", "").replace("]", "")
        issn = issn.replace(" ", "").split(",")
        

        print(issn)

        noffsets=1
        if expected_papers/1000 >=1:
            noffsets = expected_papers//1000
        # jinfo = get_papers(issn)
        cr = Crossref()
        print(f"Searching for papers in {journal_title} since 01-01-2010")
        for iss in issn:
            jinfo = cr.journals(
                ids=issn,
                works=True,
                sort="published",
                order="asc",
                cursor="*",
                cursor_max=int(expected_papers),
                filter = {'from-pub-date': '2010-01-01'},
                progress_bar = True,
                limit=1000)
            
            print(type(jinfo))
            print(iss)

            if type(jinfo) == dict:
                items = jinfo["message"]["items"]
                if len(items) > 0:
                    break
            else:
                print(sum(len(z["message"]["items"]) for z in jinfo))

                items = [z["message"]["items"] for z in jinfo]
                items = list(itertools.chain.from_iterable(items))
            

        papers = {}

        keys = [
            "title",
            "published",
            "DOI",
            "type",
            #"abstract",
            "link",
            "is-referenced-by-count",
            "publisher",
            "author" # TODO: format
        ]
        for key in keys:
            papers[key] = []
        n=1
        for item in items:
            for key in keys:
                try:
                    value = item[key]
                    if key=="title":
                        value = value[0]
                    elif key in ("published", "issued"):
                        value = value["date-parts"][0]
                        if len(value) == 3:
                            value = f"{value[0]}-{value[1]}-{value[2]}"
                        elif len(value) == 2:
                            value = f"{value[0]}-{value[1]}"
                        else:
                            value = f"{value[0]}"
                    elif key == "link":
                        for v in value:
                            # print(v["URL"])
                            if "xml" not in v["URL"]:
                                value = v["URL"]
                            if "pdf" in v["URL"]:
                                value = v["URL"]
                                break
                            else:
                                value="no link"

                    if key == "author":
                        author_string=""
                        for a in value:
                            author_string+=a["given"] + " "
                            author_string+=a["family"]
                            if a["affiliation"] != []:
                                author_string+=" (" + str(a["affiliation"][0]["name"]) + "),"                    
                        value= author_string

                    papers[key].append(value)
                except KeyError:
                    # print(f"KeyError: {key}")
                    if key == "link":
                        key="URL"
                        try:
                            papers["link"].append(item[key])
                        except KeyError:
                            papers[key].append("")
                    else:
                        papers[key].append("")

            #print([item[k] for k in keys])

        jdf = pd.DataFrame(papers)
        jj = journal_title.replace(" ", "_")
        idx_ = i+1
        jdf.to_csv(f"data/papers/{idx_:03d}_{jj}.csv", sep=",", quoting=2)

    return "done!"


def custom_tokenizer(text):
    pattern = r"(?u)\b\w\w+\b[!]*"
    return re.findall(pattern, text) 

def gather_journal_info(list_of_journals, path_to_save=None):
    ISSNs = []
    titles = []
    query = []
    available = []
    dois = []
    number_of_papers_since_2010 = []
    journals = tqdm(list_of_journals, colour="green")

    for i in journals:
        jinfo = get_journal_info(i)

        if jinfo['message']["total-results"] > 0:

            # find item wit the most similar title
            # finding the right journal
            # in majority of cases the idx of the most similar journal title
            # will be 0, however sometimes API returns more popular journal
            # title as the first choice therefore an similarity checks between
            # query and result needs to be performed
            titles_ = [j["title"] for j in jinfo["message"]["items"]]
            qq = i
            vectorizer = TfidfVectorizer(
                tokenizer=custom_tokenizer, token_pattern=None)
            combined_list = titles_ + [qq]
            tfidf_matrix = vectorizer.fit_transform(combined_list)
            # print(tfidf_matrix)
            cosine_sim = cosine_similarity(
                tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

            idx = cosine_sim.argmax()
            # sanity check
            # if idx!=0:
            #     print(titles_)
            #     print(cosine_sim)
            ### idx points to the most similiar title
            
            available.append(1)
            ISSNs.append(jinfo['message']['items'][idx]['ISSN'])
            titles.append(jinfo['message']['items'][idx]['title'])
            
            npapers = 0
            dj = jinfo[
                "message"
                ]["items"][idx]["breakdowns"]["dois-by-issued-year"]
            for year in dj:
                if int(year[0]) >= 2010:
                    npapers += year[1]
            number_of_papers_since_2010.append(npapers)
            # print(
            #     i, "|",
            #     jinfo['message']["total-results"], "|",
            #     npapers, "|",
            #     titles[-1], "|",
            #     idx)
            res = jinfo['message']["total-results"]
            journals.set_description(
                f"{i} | {res} | {npapers} | {titles[-1]} | {idx}"
                )

        else:
            available.append(0)
            ISSNs.append("")
            titles.append("")
            number_of_papers_since_2010.append("")
            # print(
            #     i,
            #     jinfo['message']["total-results"]
            #     )
            journals.set_description(f"{i} | no result found")
        query.append(i)

    df = pd.DataFrame({
        "Journal query": query,
        "Title": titles,
        "ISSN": ISSNs,
        "Available": available,
        "Number of papers since 2010": number_of_papers_since_2010
    })
    # drop duplicate rows
    # df.drop_duplicates()
    if path_to_save:
        df.to_csv(path_to_save)
    return df

def download_paper(doi, output_dir):
    cr = Crossref()
    doi = doi
    paper = cr.works(ids=doi)
    
    # print(paper)
    # print(paper["message"]["title"])

    if "link" in paper["message"]:
        download_link = paper["message"]["link"][0]["URL"]
        print(download_link)
    elif "URL" in paper["message"]:
        download_link = paper["message"]["URL"]
        download_link = find_pdf(download_link)
    else:
        print("No download link found")
        download_link = ""

    print(download_link)
    if not os.path.exists(output_dir):
        os.system(f"mkdir {output_dir}")
    
    existing_papers = list(Path(f"{output_dir}").glob("**/*.pdf"))

    if ".pdf" in download_link:
        os.system(f"wget -P {output_dir} {download_link}")
    
    else:
        os.system(f"python -m PyPaperBot --doi='{doi}' --dwn-dir='{output_dir}'")
        os.remove(f"{output_dir}/bibtex.bib")
        os.remove(f"{output_dir}/result.csv")
        
    new_number_of_papers = len(list(Path(f"{output_dir}").glob("**/*.pdf")))
    if new_number_of_papers > len(existing_papers):
        # get path to the downloaded file that was not present before
        
        new_path = list(Path(f"{output_dir}").glob("**/*.pdf"))[-1]
        return new_path
    else:
        return "Download failed"

def find_pdf(url):
    # Requests URL and get response object
    response = requests.get(url)
    # print(response.url)

    # Parse text obtained
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hyperlinks present on webpage
    links = soup.find_all('a')

    i = 0

    # From all links check for pdf link and
    # if present download file
    the_link = ""
    for link in links:
        if ('pdf' in link.get('href', [])):
            i += 1
            # print(link.get('href', []))
            the_link = link.get('href', [])
            break
    return "http://"+urlparse(response.url).netloc+the_link
        
def download_papers(dois, output_dir):
    download_results = {"doi":[], "path": [], "result":[]}
    for doi in dois:
        result = download_paper(doi, output_dir)
        if result != "Download failed":
            download_results["doi"].append(doi)
            download_results["path"].append(result)
            download_results["result"].append("Success")
        else:
            download_results["doi"].append(doi)
            download_results["path"].append("Download failed")
            download_results["result"].append("Failed")


if __name__ == "__main__":
    # print(get_journal_info("Nature"))
    # print(get_paper_by_keyword("climate change"))
    # print(get_papers())
    # print(gather_journal_info(["Nature", "Science"]))
    print(download_paper("10.1016/j.tpb.2012.08.002", "../tests/data/papers"))
    # print(download_papers(["10.1038/nature13777"], "data/papers"))
