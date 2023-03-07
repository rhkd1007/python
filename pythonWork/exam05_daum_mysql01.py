import requests 
from bs4 import BeautifulSoup
import pymysql

#https://movie.daum.net/ranking/reservation



conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="1234",
    db="big9_db",
    charset="utf8",
    use_unicode=True
)

insert_movie = "insert into daum_movie(title,grade,reserve) value(%s,%s,%s)"
req = requests.get('https://movie.daum.net/ranking/reservation')
soup = BeautifulSoup(req.text,'html.parser')

ols = soup.find('ol',class_='list_movieranking')
rankcount = ols.find_all('div', class_='thumb_cont')

# title, grade, reserve insert 하기
cur = conn.cursor()
for i in rankcount:
    movietitle = i.find('a',class_='link_txt').get_text()
    moviegrade = i.find('span',class_='txt_grade').get_text()
    movieReser = i.find('span',{'class': 'txt_num'}).get_text()
    # movieReser = i.find('span',class_='txt_num').get_text()
    print(movietitle, moviegrade, movieReser)
    cur.execute(insert_movie,(movietitle, moviegrade, movieReser))
    conn.commit()


# ↓text가 안 뽑힘.
# req = requests.get('https://movie.daum.net/ranking/reservation')
# html = req.text
# soup = BeautifulSoup(html,'lxml')
# print(soup.find_all('li'))
# movie = []
# for i in soup.find_all('li'):
#     movie.append(i.find('a',{'class' : 'link_txt'}))
#     # print(i.find('a',{'class' : 'link_txt'}))
#     movie.append(i.find('span',{'class': 'txt_grade'}))
#     # print(i.find('span',{'class': 'txt_grade'}))
#     movie.append(i.find('span',{'class': 'txt_num'}))
#     # print(i.find('span',{'class': 'txt_num'}))

