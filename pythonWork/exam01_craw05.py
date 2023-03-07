from bs4 import BeautifulSoup
import urllib.request as req


url = 'https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC'
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')

#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > b > a
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li:nth-child(1) > a
#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li > ul > li:nth-child(2) > a

#mw-content-text > div.mw-parser-output > ul:nth-child(6) > li
#mw-content-text > div.mw-parser-output > ul:nth-child(7)
#mw-content-text > div.mw-parser-output > ul:nth-child(12)

list = soup.select('#mw-content-text > div.mw-parser-output > ul > li a')
print(list)
for i in list:
    print('- ',i.string)

    

