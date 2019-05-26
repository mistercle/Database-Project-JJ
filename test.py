# Python 샘플 코드 #

import urllib
import urllib.request
import urllib.parse


url = 'http://apis.data.go.kr/9710000/NationalAssemblyInfoService/getMemberDetailInfoList'
queryParams = '?' + urllib.parse.urlencode(
    {urllib.parse.quote_plus('ServiceKey'): 'EFEiDa%2FsoKfcHkHCFPdrq1uhm5Dvg4WUTdc0tGLiQGWQIcTm2ccucqn2lAE63wDp9hY8c1c6w2srDgMYFABgtg%3D%3D',
     urllib.parse.quote_plus('numOfRows'): '10',
     urllib.parse.quote_plus('pageNo'): '1',
     urllib.parse.quote_plus('dept_cd'): '10',
     urllib.parse.quote_plus('num'): '5'})

request = urllib.request.Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urllib.request.urlopen(request).read()
print(response_body)
