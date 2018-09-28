#! /bin/bash
genelist='file_names_16s.txt'

rm -rf 'reads'
mkdir reads

while read line; do
            echo $line
            curl http://api.metagenomics.anl.gov/1/download/$line?file=425.1 > reads/$line.fastq
done < $genelist



