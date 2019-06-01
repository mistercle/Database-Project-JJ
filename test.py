# Python 샘플 코드 #

import urllib
import urllib.request
import urllib.parse

getlist = 'getMemberCurrStateList'#국회의원 현황조회
getdetail = 'getMemberDetailInfoList'#국회의원 상세조회
getjungdang = 'getJungDangMemberCurrStateList'#소속정당별 국회의원 목록조회
getcomm = 'getCommMemberCurrStateList'#소속위원회별 국회의원 목록조회
servicekey = 'oXFNR8BgFm4XU8GWU9ipGvj20Y9fBuvytfINkjq6fASRin0xIYGyO3lUUYQiTMb4%2Fjuno0wZg7azEaby0ZnLag%3D%3D'
url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/'

"""
queryParams = '?' + urllib.parse.urlencode(
    {urllib.parse.quote_plus('ServiceKey'): 'ElKInnSVC%2Bg3qeM%2BA6D8DMEtZ%2BaJ1HAJbBww6GNmQbRtHYxZ7ndPGj5AWTnN00sHxN5NNTpnYZ3blz4cDGSA6Q%3D%3D',
     urllib.parse.quote_plus('numOfRows'): '10',
     urllib.parse.quote_plus('pageNo'): '1',
     urllib.parse.quote_plus('dept_cd'): '10',
     urllib.parse.quote_plus('num'): '5'})
"""
request = urllib.request.Request(url + getlist + '?ServiceKey=' + servicekey)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read().decode('utf8')
print(response_body)
