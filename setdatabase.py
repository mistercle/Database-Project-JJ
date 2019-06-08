import mysql.connector


def database_setting():
    cnx = mysql.connector.connect(user='root',
                                  password='123123',
                                  host='127.0.0.1',
                                  database='dbtest')
    cursor = cnx.cursor()
    return cnx, cursor