import mysql.connector
import test
"""
오픈 API에서 데이터를 받아와서 정당 테이블을 업데이트
"""



"""
getlist = 'getMemberCurrStateList'#국회의원 현황조회 method_num = 0
getdetail = 'getMemberDetailInfoList'#국회의원 상세조회 method_num = 1
getjungdang = 'getJungDangMemberCurrStateList'#소속정당별 국회의원 목록조회 method_num = 2
getcomm = 'getCommMemberCurrStateList'#소속위원회별 국회의원 목록조회 method_num = 3
getmethod = 'getLoOrProporMemberCurrStateList'#당선방법별 국회의원 목록 정보조회 method_num = 4
getlocalmen = 'getLocalMemberCurrStateList'#지역별 국회의원 목록 정보조회 method_num = 5
getparty = 'getPolySearch' #정당검색 method_num = 6
getlocal = 'getLocalSearch' #지역검색 method_num = 7
getCd = 'getMemberNameInfoList' #이름검색
"""


cnx = mysql.connector.connect(user='root', password='123123',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()
#"""
def partyset():
    #정당 코드와 이름 입력 부분
    table = "party"
    table_column = "(partyCd, partyNm) "
    insert_tuple = "INSERT into " + table + table_column + "values "
    insert_query = insert_tuple + "(%s, %s) " +"ON DUPLICATE KEY UPDATE `partyCd`= VALUES(`partyCd`);"

    items = test.getitem(6)

    for item in items :
        data_partyCd = item['polyCd']
        data_partyNm = item['polyNm']
        cursor.execute(insert_query, (data_partyCd, data_partyNm))
        cnx.commit()
    #"""
    #정당 내 국회의원 수 입력 부분
    #더민당 : 123, 자한당 ; 122, 국민의당 : 38, 정의당 : 6, 무소속 : 11
    #더민당 : 이해찬, 자한당 : 황교안, 바른미래당 : 손학규, 정의당 : 이정미, 무소속 : NULL
    update_num = "UPDATE party set partyNum = 123 where partyCd = 101182; "
    cursor.execute(update_num)
    update_num = "UPDATE party set partyNum = 122 where partyCd = 101186; "
    cursor.execute(update_num)
    update_num = "UPDATE party set partyNum = 38 where partyCd = 101192; "
    cursor.execute(update_num)
    update_num = "UPDATE party set partyNum = 6 where partyCd = 101180; "
    cursor.execute(update_num)
    update_num = "UPDATE party set partyNum = 11 where partyCd = 101030;"
    cursor.execute(update_num)
    update_num = "UPDATE party set partyNum = 0 where partyNum is NULL;"
    cursor.execute(update_num)

    #정당별 당대표 입력부분

    update_num = "UPDATE party set partyNum = 123 where partyCd = 101182; "
    cursor.execute(update_num)

    cnx.commit()




