from urllib import request
from xml.etree import ElementTree


url = "http://apis.data.go.kr/1300000/mjbJiWon/list?"
row = "numOfRows=10&" #한페이지 결과수
page = "pageNo=4&"     # 페이지 수
key = "ServiceKey=HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D"

name = "gsteukgiNm"
url_1 = url + row + page + key

print(url_1)

search_item = input()
print(search_item)
response = request.urlopen(url_1).read()
tree = ElementTree.fromstring(response)
itemElements = tree.getiterator("item")
for item in itemElements:
        name_ = item.find('gtcdNm2')
        name_ = name_.text
        if(name_ == search_item):
            result = item.find("gsteukgiNm")

print(result.text)