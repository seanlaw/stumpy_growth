#!/usr/bin/env python

import argparse
import requests
import json
from lxml import html
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-slack", help='Provide Slack token')
    args = parser.parse_args()

    page = requests.get('https://api.pepy.tech/api/projects/stumpy')
    pypi_downloads = json.loads(page.content)['total_downloads']
    pypi_downloads = int(pypi_downloads)
    #print(pypi_downloads)

    page = requests.get("https://anaconda.org/conda-forge/stumpy")
    tree = html.fromstring(page.content)
    conda_downloads = tree.xpath('/html/body/div[2]/div[2]/div/div[4]/div/div[1]/ul/li[5]/span/text()')[0]
    conda_downloads = int(conda_downloads)
    #print(conda_downloads)

    total_downloads = pypi_downloads + conda_downloads
    print(total_downloads)

    page = requests.get("https://github.com/TDAmeritrade/stumpy")
    #print(page.headers['Content-Type'])
    m = re.search('(\d+) users starred this repository', page.content.decode('utf-8'))
    if m:
        github_stars = m.groups()[0]
        print(github_stars)
