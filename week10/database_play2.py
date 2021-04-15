import os
import csv
import MySQLdb

"""
    read values from a file and put them into the symptoms table
    exit db name as needed before running
"""

db = MySQLdb.connect(host ='127.0.0.1',user='root',passwd='Ninguna69*')
cursor = db.cursor()
sqldb = "CREATE DATABASE Mental_diseases"
cursor.execute(sqldb)
maketablestr = """CREATE TABLE symptoms (id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY UNIQUE,
                    visit_id INT UNSIGNED NOT NULL,symptom VARCHAR(30) NOT NULL);"""

cursor.execute(maketablestr)
db.commit()

symptomsfile = open('symptoms.tsv','r')
sympreader =csv.reader(symptomsfile,delimiter = '\t')

for row in sympreader:
    print (row)
    id = int(row[0])
    visit_id = int(row[1])
    symptom = '\"' + row[2] +'\"'
    data = (id,visit_id,symptom)
    insertstatement = """INSERT INTO symptoms VALUES (%d,%d,%s);"""
    cur.execute(insertstatement % data)
db.commit()
db.close()
symptomsfile.close()
