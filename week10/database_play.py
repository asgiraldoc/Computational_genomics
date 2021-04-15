"""
    example of SQL
        insert new records into the patients table
"""
import MySQLdb

db = MySQLdb.connect(host ='127.0.0.1',user='root',passwd='Ninguna69*',db='axltest')
#db = MySQLdb.connect('localhost',user='tuf29449',db='wk11db')

cur =  db.cursor()

cur.execute("SELECT * FROM patients")

results = cur.fetchall()
for r in results:
    print (r)

insertstatement = """INSERT INTO patients (firstname,lastname,city,state) VALUES (%s,%s,%s,%s)"""
newvals = [('Thomas','Huxley','New York','NY'),('Jane','Goodall','Paris','France')]

for nv in newvals:
    try:
        cur.execute(insertstatement,nv)
        db.commit()
        results = cur.fetchall()
        for r in results:
            print (r)
    except MySQLdb.Error as e:
        print(e)
##        try:
##            print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
##        except IndexError:
##            print "MySQL Error: %s" % str(e)
cur.execute("SELECT * FROM patients")
results = cur.fetchall()
for r in results:
    print (r)
db.close()



