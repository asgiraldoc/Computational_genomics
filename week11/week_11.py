from Bio import Entrez
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import MySQLdb
import csv

def opentsv():
    ids_refseq=[]
    embl_refseq = {}
    with open("chro_15_biomart.txt") as f:
        f.readline()
        for line in f:
            columns = line.split()
            if len(columns) > 1:
                ids_refseq.append(columns[1])
                embl_refseq[columns[1]] = columns[0]
                
        return ids_refseq, embl_refseq

def gb_file():
    Entrez.email = "tul54064@temple.edu"
    seq = ""
    f = open("chro_15_biomart.gbk", "w")
    ids_refseq, embl_refseq = opentsv()
    fetchhandle = Entrez.efetch(db="nucleotide", id=ids_refseq, rettype="gb", retmode="text")
    seq += fetchhandle.read()
    fetchhandle.close()
    print(seq, file=f)
    f.close()

def seqrecords():
    genbank = gb_file()
    lst = []
    g = open("SeqRecords_chro_15_biomart.txt", "w")
    for index, record in enumerate(SeqIO.parse("chro_15_biomart.gbk", "genbank")):
        rr = SeqRecord(
            seq = record.seq,
            id = record.id,
            name = record.name,
            features = record.features,
            description = record.description)
        print(rr, file=g)
        lst.append(record.id)
    g.close()
    return lst

def maketvs():
    seqrecID = seqrecords()
    ids_refseq, embl_refseq =  opentsv()
    embl_ID = list(embl_refseq.keys())
    refseqID = list(embl_refseq.values())
    h = open("chro_15_biomart.tsv", "w")
    for i,j,k in zip(refseqID, embl_ID, seqrecID):
        print(i + "\t" + j  + "\t" + k, file = h)
    h.close()

def part1():
    inputtable = maketvs()
    db = MySQLdb.connect(host ='localhost',user='tul54064',passwd='tul54064')
    cur =  db.cursor()

    sqldb = "CREATE DATABASE IF NOT EXISTS tul54064_table_geneIDs;"
    cur.execute(sqldb)  

    DBase = """USE tul54064_table_geneIDs;"""
    cur.execute(DBase)

    maketablestr = """CREATE TABLE IF NOT EXISTS Gene_IDs (Ensemble_ID VARCHAR(30) NOT NULL PRIMARY KEY, RefSeq_mRNA_ID TEXT NOT NULL, SeqRecord_ID TEXT NOT NULL);"""
    cur.execute(maketablestr)
    db.commit()
    
    gene_file = open("chro_15_biomart.tsv",'r')
    gene_reader = csv.reader(gene_file,delimiter = '\t')

    for row in gene_reader:
        Ensemble_ID = '\"' + row[0] +'\"'
        RefSeq_mRNA_ID = '\"' + row[1] +'\"'
        SeqRecord_ID = '\"' + row[2] +'\"'
        data = (Ensemble_ID,RefSeq_mRNA_ID,SeqRecord_ID)
        insertstatement = "INSERT INTO Gene_IDs VALUES (%s,%s,%s);"
        cur.execute(insertstatement % data)
    
    db.commit()
    db.close()
    gene_file.close()

def part2():

    db = MySQLdb.connect(host ='localhost',user='tul54064',passwd='tul54064')
    cur =  db.cursor()
    DBase = """USE tul54064_table_geneIDs;"""
    cur.execute(DBase)

    maketablestr = """CREATE TABLE IF NOT EXISTS Dog_Human_Gene_IDs (Human_gene_ID VARCHAR(30) PRIMARY KEY, Dog_gene_ID TEXT NOT NULL);"""
    cur.execute(maketablestr)
    db.commit()
    
    gene_file = open("dog_human.txt",'r')
    gene_file.readline()
    gene_reader = csv.reader(gene_file,delimiter = '\t')

    for row in gene_reader:
        Human_gene_ID = '\"' + row[0] +'\"'
        Dog_gene_ID = '\"' + row[1] +'\"'
        data = (Human_gene_ID, Dog_gene_ID)
        insertstatement = "INSERT INTO Dog_Human_Gene_IDs VALUES (%s,%s);"
        cur.execute(insertstatement % data)
    
    db.commit()
    db.close()
    gene_file.close()

def part3():


    db = MySQLdb.connect(host ='localhost',user='tul54064',passwd='tul54064')
    cur =  db.cursor()
    DBase = """USE tul54064_table_geneIDs;"""
    cur.execute(DBase)
    query =  """CREATE TABLE Inner_join AS SELECT Gene_IDs.RefSeq_mRNA_ID, Dog_Human_Gene_IDs.Dog_gene_ID FROM Gene_IDs INNER JOIN Dog_Human_Gene_IDs ON Gene_IDs.Ensemble_ID = Dog_Human_Gene_IDs.Human_gene_ID;"""
    cur.execute(query) 

    ask = input("Do you have admin permissions? yes/no: ")

    if ask == "yes":
        table_search = """ SELECT *  FROM  Inner_join INTO OUTFILE '/var/lib/mysql-files/query_inner_join.txt' """  ### I only found this solution to extract the file (in other way I got this error Error Code: 1290. )
        cur.execute(table_search) 
        db.commit()
        db.close()
    else:
        print("sorry, you need admin permissions to save this query as a file")

if __name__ == "__main__":
    part1()
    part2()
    part3()
