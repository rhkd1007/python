import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/obs-climate/land/city-obs.do'
r = requests.get(url)
ht = r.text
so = BeautifulSoup(ht,'html.parser')

# 이름, 현재기온, 습도
#weather_table > tbody > tr:nth-child(1) > td:nth-child(1) > a
#weather_table > tbody > tr:nth-child(1) > td:nth-child(6)
#weather_table > tbody > tr:nth-child(1) > td:nth-child(11)

tbody = so.select_one('tbody')
txt = []
for i in tbody.select('tr'):
    weather_td = i.select('td')
    name = weather_td[0].string
    tem = weather_td[5].string
    moi = weather_td[10].string
    txt.append([name,tem,moi])
print(txt)

weather_pandas = pd.DataFrame(txt,columns=('이름','현재기온','습도'))
print(weather_pandas)

# weather_pandas.to_csv('weather.csv')
# ↑select를 이용
# ↓find를 이용
datas = []
table = so.find('table',{'class':'table-col'})
print(table)
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    if len(tds) > 0:
        print('지역 = ', tds[0].text)
        print('온도 = ', tds[5].text)
        print('습도 = ', tds[-4].text)
        print()
        datas.append([tds[0].text, tds[5].text, tds[-4].text])

print(datas)

df = pd.DataFrame(datas, columns=('point','temp','hum'))
# df.to_csv('weather_find.csv', encoding='euc-kr', index=False)

wdf = pd.read_csv('weather_find.csv', encoding='euc-kr')
print(wdf)
#####################
print('----------------------------------')
# with open('weather_file.csv','w') as file:
#     print('파일저장')
#     file.write('point, temp, hum\n')
#     for item in datas:
#         row = ','.join(item)
#         file.write(row+'\n')

file_df = pd.read_csv('weather_file.csv', encoding='euc-kr')
print(file_df)