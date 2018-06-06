
import urllib.request
import xml.etree.ElementTree as etree
import urllib.parse

# ==========================================================================================================================================
url = "http://apis.data.go.kr/1300000/mjbJiWon/list?"
row = "numOfRows=20000&" #한페이지 결과수
# 데이터 개수 제한 43976
page = "pageNo="     # 페이지 수
key = "&ServiceKey=HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D"
# ==========================================================================================================================================

my_tf = False
filename = "militarydata.xml"
data_node = []

def readytPasing():
    global root
    global data_node
    #렉으로 인해 약 26개 중 1개로만 하여 검색
    for a in range(1, 2):
        url_1 = url + row + page + str(a) + key
        data = urllib.request.urlopen(url_1).read()

        f = open(filename, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
        f.write(data)
        f.close()

        tree = etree.parse(filename)
        root = tree.getroot()

        # 파싱해서얻어올것
        # print(root.findall(''))



def Search_item(data_name):
    print("출력중")
    data_node = []
    for a in root.findall('.//item'):

        if data_name in str(a.findtext('gtcdNm2')):
            a1 = a.findtext('gsteukgiNm')
            a2 = a.findtext('gtcdNm1')
            a3 = a.findtext('gtcdNm2')
            data_node.append([a1, a2, a3])
            print(a1)
            print(a2)
            print(a3)

    print("출력완료")
    return data_node

def Get_data(data):
    return data
# ======================================================================================================= 파일 입력
# 파싱하기