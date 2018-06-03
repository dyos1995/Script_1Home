
import urllib.request
from lxml import etree


url = "http://apis.data.go.kr/1300000/mjbJiWon/list?"
row = "numOfRows=10&" #한페이지 결과수
page = "pageNo=4&"     # 페이지 수
key = "ServiceKey=HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D"

name = "gsteukgiNm"
url_1 = url + row + page + key

data = urllib.request.urlopen(url_1).read()

filename = "Hospitaldata.xml"
f = open(filename, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
f.write(data)
f.close()

# 파싱하기
tree = etree.parse(filename)
root = tree.getroot()

# 파싱해서얻어올것
# print(root.findall(''))
for a in root.findall('.//item'):
    print("주소:", a.findtext('addr'))
    print("읍면동 :", a.findtext('emdongNm'))
    print("전화번호 :", a.findtext('telno'))
    print("병원이름 :", a.findtext('yadmNm'))
    print("병원종류 :", a.findtext('clCdNm'))
    print('----------------------')