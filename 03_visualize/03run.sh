#!/usr/bin/env bash

# Setup
mkdir -p data results

#retrieve data from 02_parse_pdb (tab seperated .csv file) to data directory 
cp ../02_parse_pdb/results/relative_frequency.csv ./data/AArelative_frequency.csv

#Run python plot script with the .csv file as an input -> output a graph in pdf
python ../bin/plot_multibar.cpython-37.pyc ./data/AArelative_frequency.csv > ./results/AA_frequencies.pdf 