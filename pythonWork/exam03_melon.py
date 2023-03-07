import pandas as pd
import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/index.htm'
r = requests.get(url,headers=header)
ht = r.text
so = BeautifulSoup(ht,'html.parser')
# print(so)

#conts
#lst50
#frm > div > table > tbody
#lst50 > td:nth-child(2) > div > span.rank
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
music_list = so.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
# print(music_list)
for idx, i in enumerate(music_list, 1):
    print(idx, i.text)



