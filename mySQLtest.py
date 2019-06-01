import mysql.connector

cnx = mysql.connector.connect(user='root', password='123123',
                              host='127.0.0.1',
                              database='SangminTest')
cursor = cnx.cursor()
query = "SELECT * FROM hip"
cursor.execute(query)
for (id, name, text, tt) in cursor:
    print("%d %s %s" % (id, name, text))

cursor.close()
cnx.close()
