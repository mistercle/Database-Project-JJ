import mysql.connector
import test
from setdatabase import database_setting
"""
오픈 API에서 데이터를 받아와서 DB를 업데이트하는 파일
"""

def assemblymanset(cnx, cursor):
    cnx, cursor = database_setting()

    table = "assemblyman"
    table_column = "(assemblymanCd, empNm, partyNm, reeleGbnNm, origCd, hobbyNm) "
    insert_tuple = "INSERT into " + table + table_column + "values"
    query = insert_tuple + "(%s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE assemblymanCd = assemblymanCd;"
    items0 = test.getitem(0)

    for i, item in enumerate(items0):
        data_assemblymanCd = item['num']
        data_empNm = item['empNm']
        data_partyNm, data_hobbyNm = test.getpartyCd(data_assemblymanCd, item['deptCd'])
        data_reeleGbNm = item['reeleGbnNm']
        data_origNm = item['origNm']
        cursor.execute("select runningAreaCd from runningarea where runningarea.runningAreaNm = '" + data_origNm + "';")
        origCd = cursor.fetchall()
        data_origCd = origCd[0][0]
        cursor.execute(query, (data_assemblymanCd, data_empNm, data_partyNm, data_reeleGbNm, data_origCd, data_hobbyNm))
        cnx.commit()
        if i % 30 == 0:
            print("■", end="")


if __name__ == "__main__":
    cnx, cursor = database_setting()
    assemblymanset(cnx, cursor)