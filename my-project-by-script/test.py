from urllib import request
from xml.etree import ElementTree


url = "http://apis.data.go.kr/1300000/mjbJiWon/list?"
row = "numOfRows=1&" #한페이지 결과수
page = "pageNo=1&"     # 페이지 수
key = "ServiceKey=HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D"

name = "gsteukgiNm"
url_1 = url + row + page + key

response = request.urlopen(url_1).read()
tree = ElementTree.fromstring(response)
itemElements = tree.getiterator("item")



print(response)
print(itemElements)