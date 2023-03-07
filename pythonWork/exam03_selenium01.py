from selenium import webdriver as wd
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv

path = "C:\pythonWork\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# print(driver)
driver.get('https://www.melon.com/chart/index.htm')
page = driver.page_source

soup = BeautifulSoup(page, 'html.parser')
# print(soup)

# 순위, 곡정보, 앨범, 좋아요수(50개 만)
# lst50
trs = soup.select('#lst50')
datas = []
for i in trs:
    #lst50 > td:nth-child(2) > div > span.rank
    rank = i.select_one('span.rank').get_text()
    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
    name = i.select_one('div.ellipsis.rank01 > span > a').get_text()

    # #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
    # singer = i.select_one('div.ellipsis.rank02 > a').get_text()
    # singer는 2개 다 가능

    #lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > span > a
    singer = i.select_one('div.ellipsis.rank02 > span > a').get_text()
    #lst50 > td:nth-child(7) > div > div > div > a
    album = i.select_one('div.rank03 > a').get_text()
    #lst50 > td:nth-child(8) > div > button > span.cnt
    likes = i.select_one('span.cnt').get_text()
    likes = re.sub('\n총건수\n','',likes)
    likes = re.sub(',','',likes)
    # print(rank, name, singer, album, likes)
    datas.append([rank, name, singer, album, likes])

print(datas)

# melon.csv

# with open : melon_file.csv
with open ('melon_file.csv','w',encoding='utf-8-sig') as file:
    file.write('순위 곡명 가수 앨범 좋아요\n')
    for item in datas:
        row = ','.join(item)
        file.write(row+"\n")
    

# pandas : melon_pandas.csv
datas_df = pd.DataFrame(datas, columns=('순위','곡명','가수', '앨범', '좋아요'))
datas_df.to_csv('melon_pandas.csv', encoding='utf-8-sig', index=False)

df = pd.read_csv('melon_pandas.csv',encoding='utf-8-sig')
print(df)
