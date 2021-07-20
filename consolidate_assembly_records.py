#! /usr/bin/env python3
import sys
import os
import numpy as np
import pandas as pd
import argparse

def get_list_of_csvs(dir_name):
    print('nice')
   

def create_master_csv(list_of_csv_files):
    print('okie_doke')
    print('outfile+"_contig_stats.csv" [:-17]')

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
    
