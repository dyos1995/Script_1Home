from tkinter import *
from tkinter import font
import tkinter.messagebox

from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus
from xml.etree import ElementTree
#from mail import *

key = 'HLlS60zzsxYZkqh4LVPkBQ60VtdA44bGdv65AfmojamkRl4qu1n1uaCLdJfY5GKZleapeEjVacbJgf2M23da5g%3D%3D'
url = 'http://apis.data.go.kr/1300000/MachumTG/list'

queryParams = '?' + urlencode({ quote_plus('ServiceKey') : key, quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1' })


request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)