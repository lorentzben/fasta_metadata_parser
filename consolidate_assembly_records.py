#! /usr/bin/env python3
import sys
import os
import numpy as np
import pandas as pd
import argparse
import glob
from pathlib import Path

def get_list_of_csvs(dir_name):
    p = Path.cwd()
    list_of_csvs = list(p.glob(dir_name+"/*_contig_stats.csv"))
    return list_of_csvs
   

def create_master_csv(list_of_csv_files, outfile):
    
    result = pd.DataFrame()
    for record in list_of_csv_files: 

        file_name = str(list_of_csvs[0]).split('/')[file_name].split('_contig')[0]
        tmp = pd.read_csv(record)
        tmp['file'] = file_name

        result = result.append(tmp)

    result.to_csv(outfile, index=False)

if __name__ == "__main__":
    try:
        inDir = sys.argv[1]
    except IndexError:
        print("Error Dir not found or provided")
        exit(1)
    try:
        outfile = sys.argv[2]
    except IndexError:
        outfile = inDir

    csv_list = get_list_of_csvs(inDir)

    create_master_csv(csv_list, outfile)
    
