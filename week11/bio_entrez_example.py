"""
    user Entrez tools to search NCBI for genes associated with a disease

    get the accession #'s for those genes

    fetch genbank records for those genes

    put them in a dictionary
"""

import time
from Bio import SeqIO   ## frmo BioPython import the SeqIO module. Used to import sequence data into a BioPython class called a SeqRecord

from Bio import Entrez
Entrez.email = "hey@temple.edu" ##online requrests using Entrez  should include a valid email address

## search the nucleotide data base for sequences from Humans that have "type II diabetes"  somewhere in the text and have a CDS in their feature table
resulthandle = Entrez.esearch(db="nucleotide", retmax=10, term=""" ((("type II diabetes")) AND txid9606 AND CDS[Feature key] """)
ereaddic = Entrez.read(resulthandle)  ## make a dictionary from the results.
resulthandle.close()

## get accession numbers for the Gene ID numbers in ereaddic["IdList"]
fetchhandle = Entrez.efetch(db="nucleotide", id=ereaddic["IdList"], rettype="acc")
accnums = fetchhandle.read().splitlines()
fetchhandle.close()
print (len(accnums), " accession numbers")
## make a dictionary to hold the genbank records
srdic = {}
for accnum in accnums:
    print (accnum," ",end="")
    try:
        fetchhandle = Entrez.efetch(db="nucleotide", id=accnum, rettype="gb", retmode="text")
        gbrecord = SeqIO.read(fetchhandle, "genbank")
        fetchhandle.close()
        srdic[gbrecord.id] = gbrecord
        print (gbrecord.description, end = "")
        print (" found")
    except:
        print (" not found")
    time.sleep(0.5) # avoid submitting too many requests in a short period of time
