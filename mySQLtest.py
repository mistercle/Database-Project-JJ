import mysql.connector

cnx = mysql.connector.connect(user='root', password='flalxlem116',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

table = "table1"
table_column = "(id)"

insert_tuple = "INSERT into" + table + table_column + "values"

query = insert_tuple + "(%d)"
cursor.execute(query, (2))
#cursor.execute(query, (4))
#for (id) in cursor:
#    print("%d" % (id))

cursor.close()
cnx.close()
