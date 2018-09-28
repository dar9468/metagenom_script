
import os
import pandas as pd
import gzip
import re


path_folder = ''
path_read = os.path.join(path_folder, '29404425')
path_read_rem = os.path.join(path_folder, '29404425_rem')
if not os.path.exists(path_read_rem):
    os.makedirs(path_read_rem)
primer_first_re = 'GTGCCAGC[A-Z]GCCGCGGTAA'
primer_second_re = 'GGACTAC[A-Z].GGGT[A-Z]TCTAAT'
primer_first = 'GTGCCAGCMGCCGCGGTAA'
primer_second = 'GGACTACHVGGGTWTCTAAT'

columns_name = ['#SampleID', 'BarcodeSequence', 'LinkerPrimerSequence']

list_result = []


for file in os.listdir(path_read):
	list_file = []
	file_name = file.rstrip('.gz').rstrip('.fastq')
	print(file_name)
	with gzip.open(os.path.join(path_read, file), 'r') as f_in:
		content = f_in.readlines()
		for line in content:
			line_str = line.decode("utf-8")
			if re.findall(primer_first_re, line_str):
				barcode = re.split(primer_first_re, line_str)[0]
				barcode_result = [file_name, barcode, primer_first]
				if barcode_result not in list_result:
					list_result.append(barcode_result)
				list_file.append(re.split(primer_first_re, line_str)[-1])
			elif re.findall(primer_second_re, line_str):
				barcode = re.split(primer_second_re, line_str)[0]
				barcode_result = [file_name, barcode, primer_second]
				if barcode_result not in list_result:
					list_result.append(barcode_result)
				list_file.append(re.split(primer_second_re, line_str)[-1])
			else:
				list_file.append(line_str)
	with open(os.path.join(path_read_rem, '{}.fastq'.format(file_name)), 'w') as f_on:
		stop = len(list_file)
		for i, li in enumerate(list_file):
			if i in range(1, stop, 4):
				len_new = len(li)
				f_on.write("{}".format(li))
			elif i in range(3, stop, 4):
				count = len(li) - len_new 
				f_on.write("{}".format(li[count:]))
			else:
				f_on.write("{}".format(li))

data = pd.DataFrame(list_result, columns=columns_name)

data.drop_duplicates(inplace=True)

data.to_csv(os.path.join(path_folder, 'barcode_new.txt'), sep='\t', index=False)

