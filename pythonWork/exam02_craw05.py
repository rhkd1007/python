import requests
from bs4 import BeautifulSoup

#########################
# 252670  251340
# [['KODEX 200선물인버스2X', '2,810'],['KODEX 코스닥150선물인버스', '4,755']]
code = ['252670', '251340']
results = []
for i in code:
    url = 'https://finance.naver.com/item/main.naver?code='+i
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string
    # print(soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a').string)
    today = soup.select_one('div > p.no_today')
    price = today.select_one('span.blind').get_text()
    # print(price.get_text())
    results.append([name, price])

print(results)
