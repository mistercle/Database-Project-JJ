import json
import urllib.request
import urllib.parse
import xmltodict

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

