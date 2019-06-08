import mysql.connector
import test
import json
import urllib.request
import urllib.parse
import xmltodict
"""
오픈 API에서 데이터를 받아와서 정당 테이블을 업데이트
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

servicekey = 'oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/'



cnx = mysql.connector.connect(user='root', password='flalxlem116',
                              host='127.0.0.1',
                              database='mydb')
cursor = cnx.cursor()

select_query = "select provinceCd from province;"
cursor.execute(select_query)
provinceList = cursor.fetchall()


table = "runningarea"
table_column = "(runningAreaCd, RunningAreaNm, provinceCd)"
insert_query = "INSERT INTO " + table + table_column + " values(%s, %s, %s);"

for i, provinceCd in enumerate(provinceList):
    request = urllib.request.Request(
            url + getlocal + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1"
            + "&" + "up_orig_cd=" + provinceCd[0])
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read().decode('utf8')
    dict_type = xmltodict.parse(response_body)
    json_type = json.dumps(dict_type)
    dict2_type = json.loads(json_type)
    items = dict2_type['response']['body']['items']['item']
    for item in items:
        data_runningAreaCd = item['origCd']
        data_runningAreaNm = item['origNm']
        data_provinceCd = provinceCd[0]
        cursor.execute(insert_query, (data_runningAreaCd, data_runningAreaNm, data_provinceCd))
        cnx.commit()

