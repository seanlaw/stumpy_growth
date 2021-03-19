#!/usr/bin/env python

import requests
import json
from lxml import html
import re
from datetime import date

if __name__ == '__main__':

    today = date.today()
    out = f"{today}\n"

    page = requests.get('https://api.pepy.tech/api/projects/stumpy', verify=False)
    pypi_downloads = json.loads(page.content)['total_downloads']
    pypi_downloads = int(pypi_downloads)
    #print(pypi_downloads)
    
    out += f"PyPI Downloads: {pypi_downloads}\n"

    page = requests.get("https://anaconda.org/conda-forge/stumpy", verify=False)
    tree = html.fromstring(page.content)
    #conda_downloads = tree.xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[1]/ul/li[2]/span/text()')[0]
    conda_downloads = tree.xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[1]/ul/li[5]/span/text()')[0]
    conda_downloads = int(conda_downloads)
    #print(conda_downloads)

    out += f"Conda Downloads: {conda_downloads}\n"

    total_downloads = pypi_downloads + conda_downloads
    #print(total_downloads)
    
    out += f"Total Downloads: {total_downloads}\n"

    page = requests.get("https://api.github.com/repos/TDAmeritrade/stumpy", verify=False)
    github_stars = json.loads(page.content)['stargazers_count']
    
    out += f"Github Stars: {github_stars}\n"

    # page = requests.get("https://badge.dimensions.ai/details/id/pub.1118108310/metrics.json", verify=False)
    # citations = json.loads(page.content)['times_cited']
    # out += f"Total Citations: {citations}\n"

    print(out)
