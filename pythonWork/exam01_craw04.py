from bs4 import BeautifulSoup
import urllib.request as req


url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
# print(res)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)

print('환율 : ',soup.select_one('span.value').string)

#exchangeList > li.on > a.head.usd > div > span.value
print('환율 value : ',soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').string)

#exchangeList > li.on > a.head.usd > div > span.blind
print('환율 blind : ',soup.select_one('#exchangeList > li.on > a.head.usd > div > span.blind').string)

value1 = soup.select('#exchangeList > li.on > a.head.usd > div > span')
print('환율1 value : ', value1[0].string)
print('blind value : ', value1[3].string)