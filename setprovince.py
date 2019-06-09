import mysql.connector
import test
from setdatabase import database_setting
"""
오픈 API에서 데이터를 받아와서 정당 테이블을 업데이트
"""

def provinceset(cnx, cursor):
    cnx, cursor = database_setting()
    array = [["021001", "서울광역시"], ["021002", "부산광역시"], ["021003", "대구광역시"], ["021004", "인천광역시"], ["021005", "광주광역시"], ["021006", "대전광역시"], ["021007", "울산광역시"], ["021008", "경기도"], ["021009", "강원도"], ["021010", "충청북도"], ["021011", "충청남도"], ["021012", "전라북도"], ["021013", "전라남도"], ["021014", "경상북도"], ["021015", "경상남도"], ["021016", "제주도"], ["021017", "비례대표"]]
    table = "province"
    table_column = "(provinceCd, provinceNm) "
    insert_tuple = "INSERT into " + table + table_column + "values "
    insert_query = insert_tuple + "(%s, %s) ON DUPLICATE KEY UPDATE provinceCd = provinceCd;"

    for i, value in enumerate(array):
        data_provinceCd = array[i][0]
        data_provinceNm = array[i][1]
        cursor.execute(insert_query, (data_provinceCd, data_provinceNm))
        cnx.commit()

    cursor.execute(insert_query, ("021018", "세종특별자치시"))
    cnx.commit()


if __name__ == "__main__":
    cnx, cursor = database_setting()
    provinceset(cnx, cursor)
