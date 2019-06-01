import mysql.connector
import test
"""
getlist = 'getMemberCurrStateList'#국회의원 현황조회 method_num = 0
getdetail = 'getMemberDetailInfoList'#국회의원 상세조회 method_num = 1
getjungdang = 'getJungDangMemberCurrStateList'#소속정당별 국회의원 목록조회 method_num = 2
getcomm = 'getCommMemberCurrStateList'#소속위원회별 국회의원 목록조회 method_num = 3
getmethod = 'getLoOrProporMemberCurrStateList'#당선방법별 국회의원 목록 정보조회 method_num = 4
getlocalmen = 'getLocalMemberCurrStateList'#지역별 국회의원 목록 정보조회 method_num = 5
getparty = 'getPolySearch' #정당검색 method_num = 6
getlocal = 'getLocalSearch' #지역검색 method_num = 7
"""

cnx = mysql.connector.connect(user='root', password='flalxlem116',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

table = "datalist"
table_column = "(num, name)"
insert_tuple = "INSERT into " + table + table_column + "values "
query = insert_tuple + "(%s, %s)"
items = test.getitem(0)
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