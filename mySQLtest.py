import mysql.connector

cnx = mysql.connector.connect(user='root', password='123123',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()
query = "SELECT * FROM party"
cursor.execute(query)
for (partyCd, partyNm) in cursor:
    print("%s %s" % (partyCd, partyNm))

cursor.close()
cnx.close()
