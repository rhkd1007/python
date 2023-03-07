import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://m.dhlottery.co.kr/gameResult.do?method=byWin'
r = requests.get(url)
ht = r.text
so = BeautifulSoup(ht,'html.parser')

