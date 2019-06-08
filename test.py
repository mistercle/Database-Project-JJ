# Python 샘플 코드 #
import json
import urllib.request
import urllib.parse
import xmltodict


servicekey = 'oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/'

getlist = 'getMemberCurrStateList'  # 국회의원 현황조회 method_num = 0
getdetail = 'getMemberDetailInfoList'  # 국회의원 상세조회 method_num = 1
getjungdang = 'getJungDangMemberCurrStateList'  # 소속정당별 국회의원 목록조회 method_num = 2
getcomm = 'getCommMemberCurrStateList'  # 소속위원회별 국회의원 목록조회 method_num = 3
getmethod = 'getLoOrProporMemberCurrStateList'  # 당선방법별 국회의원 목록 정보조회 method_num = 4
getlocalmen = 'getLocalMemberCurrStateList'  # 지역별 국회의원 목록 정보조회 method_num = 5
getparty = 'getPolySearch'  # 정당검색 method_num = 6
getlocal = 'getLocalSearch'  # 지역검색 method_num = 7
getCd = 'getMemberNameInfoList'  # 이름검색
"""
dict_type = xmltodict.parse(response_body)
json_type = json.dumps(dict_type)
dict2_type = json.loads(json_type)
items = dict2_type['response']['body']['items']['item']
for item in items:
    print(item)
    # 이름이랑 num 만 출력
    print(item['empNm'], item['num'])
"""
def getitem(method_num):




    if method_num == 0 : #list
        request = urllib.request.Request(
            url + getlist + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items0 = dict2_type['response']['body']['items']['item']
        return items0

    elif method_num == 1 : #detail
        request = urllib.request.Request(
            url + getdetail + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items1 = dict2_type['response']['body']['items']['item']
        return items1

    elif method_num == 2 : #getjungdang
        request = urllib.request.Request(
            url + getjungdang + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items2 = dict2_type['response']['body']['items']['item']
        return items2

    elif method_num == 3 : #getcomm
        request = urllib.request.Request(
            url + getcomm + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items3 = dict2_type['response']['body']['items']['item']
        return items3

    elif method_num == 4 : #getmethod
        request = urllib.request.Request(
            url + getmethod + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items4 = dict2_type['response']['body']['items']['item']
        return items4

    elif method_num == 5 : #getlocalmen
        request = urllib.request.Request(
            url + getlocalmen + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items5 = dict2_type['response']['body']['items']['item']
        return items5

    elif method_num == 6 : #getparty
        request = urllib.request.Request(
            url + getparty + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items6 = dict2_type['response']['body']['items']['item']
        return items6

    elif method_num == 7:  # getlocal
        request = urllib.request.Request(
            url + getlocal + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
            + "&" + "numOfRows=300"
            + "&" + "pageNo=1")
        request.get_method = lambda: 'GET'
        response_body = urllib.request.urlopen(request).read().decode('utf8')
        dict_type = xmltodict.parse(response_body)
        json_type = json.dumps(dict_type)
        dict2_type = json.loads(json_type)
        items7 = dict2_type['response']['body']['items']['item']
        return items7

    else :
        print("Method_num is uncorrect!!")
        exit(1)
#정당과 취미 검색
def getpartyCd(num, deptCd):
    request = urllib.request.Request(
        url + getdetail + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
        + "&" + "numOfRows=300"
        + "&" + "pageNo=1"
        + "&" + "dept_cd=" + deptCd
        + "&" + "num=" + num)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read().decode('utf8')
    dict_type = xmltodict.parse(response_body)
    json_type = json.dumps(dict_type)
    dict2_type = json.loads(json_type)
    item = dict2_type['response']['body']['item']
    party = item['polyNm']
    return party

def gethobbyCd(num, deptCd):
    request = urllib.request.Request(
        url + getdetail + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
        + "&" + "numOfRows=300"
        + "&" + "pageNo=1"
        + "&" + "dept_cd=" + deptCd
        + "&" + "num=" + num)
    request.get_method = lambda: 'GET'
    response_body = urllib.request.urlopen(request).read().decode('utf8')
    dict_type = xmltodict.parse(response_body)
    json_type = json.dumps(dict_type)
    dict2_type = json.loads(json_type)
    item = dict2_type['response']['body']['item']
    try:
        hobbyCd = item['hbbyCd']
    except KeyError:
        hobbyCd = "없음"
    return hobbyCd

#def getorigCd():

#def getre
