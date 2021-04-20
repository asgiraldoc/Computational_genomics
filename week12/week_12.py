from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import Entrez
from Bio import SeqIO

def readfile():
    with open ("ch_ests_3.fasta") as f:
        dic_seq = {}
        seq = ""
        for lines in f:
            line = lines.rstrip()
            if line.startswith(">"):
                gi, gi_num, gb, acc_num, descrip = line.split("|")
                dic_seq[acc_num] = ""
                seq = acc_num
            else:
                if dic_seq[seq] =="":
                    dic_seq[seq] = line
                else:
                    dic_seq[seq] += line                 
        return dic_seq

def blastx():
    query = readfile()
    dic_ortho = {}
    for i,j in query.items():
        print(i)
        blast_result_handle = NCBIWWW.qblast(program="blastx",database="refseq_protein",sequence= j,entrez_query= "txid9606[ORGN]")
        blast_records = NCBIXML.parse(blast_result_handle)
        blast_record = next(blast_records)
        for alignment in blast_record.alignments[0:1]:
            rr = alignment.hit_id
            gi, id, nu = rr.split("|")
            dic_ortho[i] = id
    return dic_ortho


def main():
    Entrez.email = "tul54064@temple.edu"
    acc_num = blastx()
    dic_ID = {}
    for i, j in acc_num.items():
        search_term = j
        handle = Entrez.esearch(db='Protein', term=search_term)
        result = Entrez.read(handle)["IdList"]
        result1 = "".join(result)
        dic_ID[i] = result1
        handle.close()
    fill = {key: dic_ID[key] + "\t" + acc_num.get(key, '') for key in dic_ID.keys()}
    f = open("table.txt", "w")
    for i, j in fill.items():
        print(i,j)
        print(i,j, file =f)
    g = open("list.txt", "w")
    for i, j in dic_ID.items():
        print(j, file=g)
    g.close()
    f.close() 

if __name__ == "__main__":
    main()


