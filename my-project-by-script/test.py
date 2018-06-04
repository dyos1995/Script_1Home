
import urllib.request
import xml.etree.ElementTree as etree
import urllib.parse

# ==========================================================================================================================================
url = "http://apis.data.go.kr/1300000/mjbJiWon/list?"
row = "numOfRows=43976&" #한페이지 결과수
page = "pageNo="     # 페이지 수
key = "&ServiceKey=HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D"
# ==========================================================================================================================================

my_tf = False
filename = "militarydata.xml"
counter = 0



for a in range(1, 26):
    url_1 = url + row + page + str(a) + key
    data = urllib.request.urlopen(url_1).read()

    f = open(filename, "wb")  # 다른 사람들의 예제처럼 "w"만 해서 했더니 에러가 발생
    f.write(data)
    f.close()

    tree = etree.parse(filename)
    root = tree.getroot()

    # 파싱해서얻어올것
    # print(root.findall(''))
    for a in root.findall('.//item'):
        if(a.findtext('gtcdNm2') == "컴퓨터공학과"):
            print("군사특기명:", a.findtext('gsteukgiNm'))
            print("군명 :", a.findtext('gtcdNm1'))
            print("자격증전공명 :", a.findtext('gtcdNm2'))
            print("자격면허등급 :", a.findtext('jgmyeonheoDg'))
            print("직간접구분 :", a.findtext('jjganjeopGbcd'))
            print('----------------------')

# ======================================================================================================= 파일 입력
# 파싱하기



