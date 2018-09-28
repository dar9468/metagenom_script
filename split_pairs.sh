#!bin/bash 

rm -rf splitted_R1 splitted_R2
mkdir splitted_R1 splitted_R2


for file in *.fastq*; do
	echo $file
	length=$(zless $file | wc -L | cut -f1 -d ' ')
	length=$((length/2))
	echo "$file, max length divided by 2 $length"
	file_R1="${file/.fastq*/_R1.fastq}"
	file_R2="${file/.fastq*/_R2.fastq}"	
	zless $file | awk -F '\t' -v len=$length '{ if (length($1)<len) print $0"/1"; else print substr($1, 0, len)}' > splitted_R1/$file_R1
	zless $file | awk -F '\t' -v len=$length '{ if (length($1)<len) print $0"/2"; else print substr($1, len+1, 2*len)}' > splitted_R2/$file_R2
done

