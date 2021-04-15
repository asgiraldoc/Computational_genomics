import os
import csv
import MySQLdb
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="table tvs")

args = parser.parse_args()


db = MySQLdb.connect(host ='localhost',user='tul54064',passwd='tul54064')
cur =  db.cursor()

sqldb = "CREATE DATABASE IF NOT EXISTS tul54064_mental_diseases;"
cur.execute(sqldb)

DBase = """USE tul54064_mental_diseases;"""
cur.execute(DBase)

maketablestr = """CREATE TABLE Schizophrenia (Disease VARCHAR(15) NOT NULL, NCBI_accession TEXT NOT NULL,
Length INT UNSIGNED,Sequence TEXT NOT NULL);"""

cur.execute(maketablestr)
db.commit()

diseasefile = open(args.input,'r')
diseasereader = csv.reader(diseasefile,delimiter = '\t')

for row in diseasereader:
    print (row)
    Disease = '\"' + row[0] +'\"'
    NCBI_accession = '\"' + row[1] +'\"'
    Length = int(row[2])
    Sequence = '\"' + row[3] +'\"'
    data = (Disease,NCBI_accession,Length,Sequence)
    insertstatement = "INSERT INTO Schizophrenia VALUES (%s,%s,%d,%s);"
    cur.execute(insertstatement % data)
db.commit()
db.close()
diseasefile.close()
