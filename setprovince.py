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


cnx = mysql.connector.connect(user='root', password='flalxlem116',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

def provinceset():
    array = [["021001", "서울광역시"], ["021002", "부산광역시"], ["021003", "대구광역시"], ["021004", "인천광역시"], ["021005", "광주광역시"], ["021006", "대전광역시"], ["021007", "울산광역시"], ["021008", "경기도"], ["021009", "강원도"], ["021010", "충청북도"], ["021011", "충청남도"], ["021012", "전라북도"], ["021013", "전라남도"], ["021014", "경상북도"], ["021015", "경상남도"], ["021016", "제주도"]]
    table = "province"
    table_column = "(provinceCd, provinceNm) "
    insert_tuple = "INSERT into " + table + table_column + "values "
    insert_query = insert_tuple + "(%s, %s) ON DUPLICATE KEY UPDATE provinceCd = provinceCd;"

    for i in array:
        data_provinceCd = array[i][0]
        data_provinceNm = array[i][1]
        cursor.execute(insert_query, (data_provinceCd, data_provinceNm))
        cnx.commit()
