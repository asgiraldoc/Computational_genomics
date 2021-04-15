#!/bin/bash

fasta=./GRCH38p2_chr22.fasta																				##Files
fastq=./brca.example.illumina.0.1.fastq

echo 'Is your file a extension of fasta or fastq files?'						##Asking type file
read typeFile

Nucl=$(echo 'Would you like to count only one nucleotide? (yes or no)')
specNucl=$(echo 'Which one?')																			 ##Asking what you want to do

if [[ "$typeFile" == "fasta" || "$typeFile" == "fa" ]]						 ##Working on Fasta file
then
	echo $Nucl
	read Nuclefasta
	if [[ "$Nuclefasta" == "yes" ]]
	then
		echo $specNucl
		read WhichOne
		upperW=$(printf $WhichOne | tr a-z A-Z )											## upper sequence
		count=$(grep -v ^\> $fasta | tr a-z A-Z | grep -o $upperW | wc -l) ## upper input nucleotide
		echo "There are $count $upperW's in total"
	else
		allcount=$(grep -v ^\> $fasta | grep -o -e A -e T -e C -e G -e N | sort | uniq -c)  ## count nucleotides
		echo "$allcount"
	fi

elif [[ "$typeFile" == "fastq" || "$typeFile" == "fq" ]]					##Working on Fasta file
then
	echo $Nucl
	read Nuclefastq
	if [[ "$Nuclefastq" == "yes" ]]
	then
		echo $specNucl
		read WhichOne
		upperW=$(printf $WhichOne | tr a-z A-Z )											## upper sequence
		count=$(awk '(NR%4==2)' $fastq | tr a-z A-Z | grep -o $upperW | wc -l) ## upper input nucleotide
		echo "There are $count $upperW's in total"
	else
		allcount=$(awk '(NR%4==2)' $fastq | grep -o -e A -e T -e C -e G -e N | sort | uniq -c) ## count nucleotides
		echo "$allcount"
	fi

else
	echo 'Your file is not valid'
fi


#######################################
#######################################
							#RESULTS#
#######################################
#######################################


### fasta file: GRCH38p2_chr22.fasta
### Output:
### 10382214 A
### 9160652 C
### 9246186 G
### 11658686 N
### 10370725 T


### fasta file: GRCH38p2_chr22.fasta
### Output:
### 894660 A
### 706586 C
### 705697 G
### 895969 T
