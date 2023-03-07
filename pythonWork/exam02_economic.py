import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import re

req = requests.get("https://news.daum.net/economic")
soup = BeautifulSoup(req.content, 'html.parser')

links = soup.select('a[href]')
# print(links)

# 100개중 https:/v. 시작하는 기사 출력
for i in links[:100]:
    # \w 영문자 숫자 언더바(밑줄) [A-Za-Z0-9_]
    if re.search('https://v.\w+', i['href']):
        print(i.get_text().strip())
    # if re.match('https://v.\w+', i['href']):
    #     print(i.string)
