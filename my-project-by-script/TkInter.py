from tkinter import *
from tkinter import font
import tkinter.messagebox

import urllib.request
from xml.etree import ElementTree
#from mail import *


class get_military_data():
    key = 'HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D'
    url = "http://apis.data.go.kr/1300000/jBGSSCJeongBo/" % key

    def main(self):
        data = urllib.request.urlopen(self.url).read()

        f = open("sample1.xml", 'wb')
        f.write(data)
        f.close()

getData = get_military_data()
getData.main()