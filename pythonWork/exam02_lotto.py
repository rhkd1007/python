import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get("https://m.dhlottery.co.kr/gameResult.do?method=byWin")
soup = BeautifulSoup(req.text, 'html.parser')
# print(soup)

# find
ballNum = soup.find_all('span', class_='ball')
for i in ballNum:
    print(i.get_text(), end=' ') # i.string
print('\n')
# select
#container > div > div.bx_lotto_winnum
nums = soup.select('#container > div > div.bx_lotto_winnum > span.ball')
# print(nums)
for i in nums:
    print(i.get_text(), end=' ')