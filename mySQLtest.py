import mysql.connector
import test

cnx = mysql.connector.connect(user='root', password='flalxlem116',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

table = "datalist"
table_column = "(num, name)"
insert_tuple = "INSERT into " + table + table_column + "values "
query = insert_tuple + "(%s, %s)"
items = test.getitem()
for item in items :
    data_name = item['empNm']
    data_num = item['num']
    cursor.execute(query, (data_num, data_name))
    cnx.commit()


#query = insert_tuple + "(%s)"
#cursor.execute(query, 2)
#cnx.commit()


cursor.close()
cnx.close()
