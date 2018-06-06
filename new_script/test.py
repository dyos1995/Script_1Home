import os
import sys
import urllib.request
import xml.etree.ElementTree as ET

level = 10
width = 471
height = 221

client_id = "2w8gufHzxvI4OZuwlGZW" # 애플리케이션 등록시 발급 받은 값 입력
client_secret = "CwvXhM4ofs" # 애플리케이션 등록시 발급 받은 값 입력

m_filename = "naver_api_search.xml"

encText = urllib.parse.quote("불정로 6")
url = "https://openapi.naver.com/v1/map/geocode?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/map/geocode.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


