#!/usr/bin/env python

import requests
import json
from lxml import html
import re
from datetime import date

def get_pypi_downloads():
    page = requests.get('https://api.pepy.tech/api/v2/projects/stumpy', verify=False)
    downloads = json.loads(page.content)['total_downloads']
    downloads = int(downloads)
    #print(downloads)
    return downloads


def get_conda_downloads():
    page = requests.get("https://anaconda.org/conda-forge/stumpy", verify=False)
    tree = html.fromstring(page.content)
    #downloads = tree.xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[1]/ul/li[2]/span/text()')[0]
    downloads = tree.xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[1]/ul/li[5]/span/text()')[0]
    downloads = int(downloads)
    #print(downloads)
    return downloads


def get_github_stars():
    page = requests.get("https://api.github.com/repos/TDAmeritrade/stumpy", verify=False)
    github_stars = json.loads(page.content)['stargazers_count']
    return github_stars

if __name__ == '__main__':

    today = date.today()
    out = f"{today}\n"
    
    pypi_downloads = get_pypi_downloads()
    out += f"PyPI Downloads: {pypi_downloads}\n"

    conda_downloads = get_conda_downloads()
    out += f"Conda Downloads: {conda_downloads}\n"

    total_downloads = pypi_downloads + conda_downloads
    #print(total_downloads)
    
    out += f"Total Downloads: {total_downloads}\n"

    
    github_stars = get_github_stars()
    out += f"Github Stars: {github_stars}\n"

    # page = requests.get("https://badge.dimensions.ai/details/id/pub.1118108310/metrics.json", verify=False)
    # citations = json.loads(page.content)['times_cited']
    # out += f"Total Citations: {citations}\n"

    print(out)
