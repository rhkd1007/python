from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
resp = req.urlopen(url)
print(resp)
soup = BeautifulSoup(resp, 'html.parser')
# print(soup)
#title 출력
# title = soup.channel.title
title = soup.find('title').string
print(title)

#wf 출력
print(soup.find('wf').string)

