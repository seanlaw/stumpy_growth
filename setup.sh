#!/bin/sh

# Setup Conda Environment
if ! [ -x "$(command -v conda)" ]; then
    wget Miniconda3-latest-Linux-x86_64.sh
    bash ./Miniconda3-latest-Linux-x86_64.sh 
fi

conda install -y lxml
