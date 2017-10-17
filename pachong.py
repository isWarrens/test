import urllib.request
from bs4 import BeautifulSoup
import urllib.parse


url='http://news.ncu.edu.cn/'
request=urllib.request.Request(url)
response=urllib.request.urlopen(request)
html=response.read().decode('utf-8')
result0=BeautifulSoup(html,'html.parser')
result1=result0.findAll('ul',{'class':{'newslist'}})
result2=result0.findAll('ul',{'class':{'txt'}})
for finally_result0 in result1:
    print(finally_result0.get_text())
for finally_result1 in result1:
    print(finally_result1.get_text())

