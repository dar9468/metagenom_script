
import os
import pandas as pd
import gzip


path_folder = ''
path_read = os.path.join(path_folder, '29404425')
primer_first = 'GTGCCAGCMGCCGCGGTAA'
primer_second = 'GGACTAC**GGGT*TCTAAT'

columns_name = ['SampleID', 'BarcodeSequence', 'LinkerPrimerSequence']

list_result = []

for file in os.listdir(path_read):
	file_name = file.rstrip('.gz').rstrip('.fastq')
	print(file)
	list_result.append([file, '' , primer_first])

data = pd.DataFrame(list_result, columns=columns_name)

data.drop_duplicates(inplace=True)

data.to_csv(os.path.join(path_read, 'map_file.txt'), sep='\t', index=False)

