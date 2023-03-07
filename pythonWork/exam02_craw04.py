import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/main.naver?code=252670'
url1 = 'https://finance.naver.com/item/main.naver?code=251340'

r = requests.get(url)
r1 = requests.get(url1)
html = r.text
html1 = r1.text
soup = BeautifulSoup(html, 'html.parser')
soup1 = BeautifulSoup(html1, 'html.parser')
# print(soup)
title = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string)
print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').get_text())

today = soup.select_one('div > p.no_today')
price = today.select_one('span.blind')
print(price.get_text())
# print(soup.select('div > p.no_today > em > span.blind')) # string 및 get_text() 를 사용시 에러 발생
#########################
# 252670  251340
# [['KODEX 200선물인버스2X', '2,810'],['KODEX 코스닥150선물인버스', '4,755']]
