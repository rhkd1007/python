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

# ↓text가 안 뽑힘. 너무 범위가 넓어 첫번째 부터 None값이 생김.
req = requests.get('https://movie.daum.net/ranking/reservation')
html = req.text
soup = BeautifulSoup(html,'html.parser')
# print(soup.find_all('li'))

movie = []
for i in soup.find_all('li'):
    movietitle = i.find('a',{'class' : 'link_txt'})
    moviegrade = i.find('span',{'class' : 'txt_grade'})
    movieReser = i.find('span',{'class' : 'txt_num'})
    if movietitle!=None:
        movie.append(movietitle.get_text())
    # print(i.find('a',{'class' : 'link_txt'}))
    if moviegrade!=None:
        movie.append(moviegrade.get_text())
    # print(i.find('span',{'class': 'txt_grade'}))
    if movieReser!=None:
        movie.append(movieReser.get_text())
    # print(i.find('span',{'class': 'txt_num'}))
print(movie)
    

# insert_movie = "insert into daum_movie(title,grade,reserve) value(%s,%s,%s)"
# req = requests.get('https://movie.daum.net/ranking/reservation')
# soup = BeautifulSoup(req.text,'html.parser')

# ols = soup.find('ol',class_='list_movieranking')
# rankcount = ols.find_all('div', class_='thumb_cont')

# title, grade, reserve insert 하기
# cur = conn.cursor()
# for i in rankcount:
#     movietitle = i.find('a',class_='link_txt').get_text()
#     moviegrade = i.find('span',class_='txt_grade').get_text()
#     movieReser = i.find('span',{'class': 'txt_num'}).get_text()
#     # movieReser = i.find('span',class_='txt_num').get_text()
#     # print(movietitle, moviegrade, movieReser)
#     cur.execute(insert_movie,(movietitle, moviegrade, movieReser))
#     conn.commit()




