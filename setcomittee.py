from setdatabase import database_setting


def comitteeset(cnx, cursor):
    cnx, cursor = database_setting()
    array = [["130001", "국회운영위원회", "2537"],
             ["130002", "법제사법위원회", "2747"],
             ["130003", "정무위원회", "110"],
             ["130004", "기획재정위원회", "2"],
             ["130005", "교육위원회", "2540"],
             ["130006", "과학기술정보방송통신위원회", "133"],
             ["130007", "외교통일위원회", "2638"],
             ["130008", "국방위원회", "2659"],
             ["130009", "행정안전위원회", "2609"],
             ["130010", "문화체육관광위원회", "105"],
             ["130011", "농림축산식품해양수산위원회", "2811"],
             ["130012", "산업통상자원중소벤처기업위원회", "2782"],
             ["130013", "보건복지위원회", "2764"],
             ["130014", "환경노동위원회", "2630"],
             ["130015", "국토교통위원회", "114"],
             ["130016", "정보위원회", "52"],
             ["130017", "여성가족위원회", "2690"]]
    table = "comittee"
    table_column = "(comitteeCd, comitteeNm, chairmanCd) "
    insert_tuple = "INSERT into " + table + table_column + "values "
    insert_query = insert_tuple + "(%s, %s, %s) ON DUPLICATE KEY UPDATE comitteeCd = comitteeCd;"

    for i, value in enumerate(array):
        cursor.execute(insert_query, (value[0], value[1], value[2]))
        cnx.commit()

    cnx.commit()


def assemblyman_has_comitteeset(cnx, cursor):
    cnx, cursor = database_setting()
    array = []  # TODO 추가 필요
    table = "assemblyman_has_comittee"
    table_column = "(assemblymanCd, comitteeCd) "
    insert_tuple = "INSERT into " + table + table_column + "values "
    insert_query = insert_tuple + "(%s, %s)"

    for i, value in enumerate(array):
        cursor.execute(insert_query, (value[0], value[1]))
        cnx.commit()

    cnx.commit()


if __name__ == "__main__":
    cnx, cursor = database_setting()
    comitteeset(cnx, cursor)
    assemblyman_has_comitteeset(cnx, cursor)
