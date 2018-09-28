#!/usr/bin/python3

import argparse
import os
import pandas as pd

def rename_file(x, line_file, folder):
	if x['SubjectID'] in all_file_line:
		for i in [1,2]:
			name = 'CGMS.{sub}.repl{repl}fq.gz'.format(sub=x['SubjectID'],
									  repl=i)
			if os.path.exists(os.path.join(folder,name)):
				print(name)
				new_name = '{barcode}.repl{repl}.fastq.gz'.format(barcode=x['Barcode'],
									  repl=i)
				os.rename(os.path.join(folder,name),os.path.join(folder,new_name))

parser = argparse.ArgumentParser()
parser.add_argument(
    "-df",
    "--data_folder",
    type=str,
    help="A full path to folder with fastq files",
    required=True,
    action="store"
)
parser.add_argument(
    "-o",
    "--output_folder",
    type=str,
    help="Output folder",
    required=False,
    action="store",
)
parser.add_argument(
    "-m",
    "--metadata",
    type=str,
    help="Metadata",
    required=False,
    action="store",
)
args = parser.parse_args()

folder = args.data_folder
output = args.output_folder
metadata = args.metadata

metadata_table = pd.read_csv(metadata)

all_file = os.listdir(folder)
all_file_line = ';'.join(all_file)

metadata_table.apply(lambda x: rename_file(x, all_file_line, folder),axis=1)

