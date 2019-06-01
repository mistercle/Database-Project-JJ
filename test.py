# Python 샘플 코드 #
import json
import urllib.request
import urllib.parse
import xmltodict

url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberCurrStateList'

request = urllib.request.Request(url + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
                                 + "&" + "numOfRows=300"
                                 + "&" + "pageNo=1"
                                 + "&" + "dept_cd=9770372")
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read().decode('utf8')


dict_type = xmltodict.parse(response_body)
json_type = json.dumps(dict_type)
dict2_type = json.loads(json_type)
items = dict2_type['response']['body']['items']['item']
for item in items:
    print(item)
