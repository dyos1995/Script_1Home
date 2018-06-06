import urllib.request
import xml.etree.ElementTree as etree
import urllib.parse

client_id = "2w8gufHzxvI4OZuwlGZW" # 애플리케이션 등록시 발급 받은 값 입력
client_secret = "CwvXhM4ofs" # 애플리케이션 등록시 발급 받은 값 입력

m_filename = "naver_api_search.xml"

def Search_txt(data_name):
    encText = urllib.parse.quote("공공기관" + data_name + "병무청")

    url = "https://openapi.naver.com/v1/search/local.xml?query=" + encText +"&display=3&sort=count"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)

    naver_data = []
    response = urllib.request.urlopen(request).read()

    f = open(m_filename,'wb')
    f.write(response)
    f.close()

    tree = etree.parse(m_filename)
    root = tree.getroot()

    for a in root.findall('.//item'):
        if ("공공,사회기관" in str(a.findtext("category"))):
            naver_data.append([a.findtext("title"), a.findtext("telephone"), a.findtext("address"), a.findtext("roadAddress"), a.findtext("mapx"),a.findtext("mapy")])


    return naver_data

def Set_map_point(x_point, y_point):
    global level, width, height
    url_png = "https://openapi.naver.com/v1/map/staticmap.bin?clientId=" + client_id + "&url=file://c&crs=EPSG:4326&center=" + str(x_point) + "," + str(y_point) + "&level=" + str(level) + "&w=" + str(width) + "&h=" + str(height) + "&baselayer=default&markers=" + str(x_point) + "," + str(y_point)
    request = urllib.request.Request(url_png)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        return url_png
    else:
        print("Error Code:" + rescode)