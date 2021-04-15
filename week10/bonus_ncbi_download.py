from Bio import Entrez
from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("output", type=str, help="the output file in tsv format")

args = parser.parse_args()

def acc_numbers():
    Entrez.email = "tul54064@temple.edu" 
    search_term = "Schizophrenia[All Fields] AND Homo sapiens[porgn] AND biomol_mrna[PROP]"
    handle = Entrez.esearch(db='nuccore', term=search_term)
    result1 = Entrez.read(handle)["Count"]
    handle.close()

    get_num = input("How many results would you like to get (press enter to get all of them): ")
    if not get_num:
        get_num = result1
    all_ID = Entrez.esearch(db='nuccore', term=search_term, retmax=get_num)
    result = Entrez.read(all_ID)
    all_ID.close()

    fetch_handle = Entrez.efetch(db="nuccore", id=result["IdList"], rettype="acc")
    acc_ids = [id.strip() for id in fetch_handle]
    fetch_handle.close()
    return acc_ids

def get_fastas():
    seq = ""
    ids = acc_numbers()
    net_handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
    seq += net_handle.read()
    return seq

def tsv_file():
    sequences = get_fastas()
    fasta = {}
    seq = ""
    for line in sequences.split("\n"): 
        if line.startswith(">"):
            header=line.replace(">","")
            id_num = header.split(maxsplit=1)
            fasta[id_num[0]] = ""
            seq = id_num[0]
        else:
            if fasta[seq] =="":
                fasta[seq] = line
            else:
                fasta[seq] += line
    return fasta

def main():
    x = tsv_file()
    f = open(args.output,'w')
    for i,j in x.items():
        
        print("Schizophrenia" + "\t" + i + "\t" + str(len(j)) + "\t" + j, file=f)
    f.close()

if __name__ == "__main__":
    main()

