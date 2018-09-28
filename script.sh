#!/bin/bash
readslist=SRR_Acc_List.txt
srapath='sratoolkit.2.8.2-ubuntu64/bin'
reads='reads'
mkdir $reads
  
while read rfile; do
            echo $rfile
            cd $srapath
            ./prefetch $rfile
            ./fastq-dump $rfile -O $reads
            delsra=/home/ncbi/public/sra/${rfile}.sra
            rm $delsra
done < $readslist
