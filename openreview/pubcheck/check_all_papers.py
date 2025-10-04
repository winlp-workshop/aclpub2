import os
from tqdm import tqdm

import yaml


if __name__ == '__main__':
    # get all papers in "../papers" folder
    papers = [f for f in os.listdir("../papers") if f.endswith(".pdf")]
    print(f"Found {len(papers)} papers in ../papers folder")
    
    # read yml
    papers_info = yaml.safe_load(open("../papers.yml", "r"))

    file_to_archival = {}
    for p in papers_info:
        file_to_archival[p['file']] = p['archival']

    # run aclpubcheck on each paper
    # aclpubcheck --paper_type short path
    for paper in tqdm(papers):
        if paper in file_to_archival and file_to_archival[paper]:
            print(f"Checking {paper} (archival)")
            os.system(f"aclpubcheck --paper_type long ../papers/{paper} > ./pubcheck_results/{paper}.txt")
        else:
            print(f"{paper} (non-archival)")
    print("Done! Check pubcheck_results folder for results")
