import requests
from bs4 import BeautifulSoup
from xlwt import *
mylink = "https://en.wikipedia.org/wiki/Nature"
line=1
if(requests.get(mylink).status_code)==200:
    url = mylink
    code = requests.get(url)
    plain = code.text
    workbook = Workbook(encoding = 'utf-8')
    table = workbook.add_sheet('data')
    table.write(0, 0, 'Name')
    table.write(0, 1, 'Link')
    s = BeautifulSoup(plain,"html.parser")
    for m in s.findAll('a'):
        b=m.string
        print(m.string)
        c=m.get('href')
        print(m.get('href'))
        table.write(line,0,b)
        table.write(line,1,c)
        line +=1
    workbook.save('data1.xls')
    