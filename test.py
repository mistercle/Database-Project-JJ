# Python 샘플 코드 #

import urllib
import urllib.request
import urllib.parse

url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberCurrStateList'

request = urllib.request.Request(url + '?' + 'ServiceKey=oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
                                 + "&" + "numOfRow=10"
                                 + "&" + "pageNo=1")
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read().decode('utf8')
print(response_body)
