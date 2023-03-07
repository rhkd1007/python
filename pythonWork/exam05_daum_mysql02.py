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

select_movie = "select grade from daum_movie"
cur = conn.cursor()
cur.execute(select_movie)
movies = cur.fetchall()
#평점 9점이상, 8점이상, 6점이상, 6점미만 ==>pid
movieDic = {'9점이상':0, '8점이상':0, '6점이상':0, '6점미만': 0}

for movie in movies:
    movie = float(movie[0])
    if movie >= 9 :
        movieDic["9점이상"] +=1
    elif movie >= 8 :
        movieDic["8점이상"] +=1
    elif movie >= 6 :
        movieDic["6점이상"] +=1
    else :
        movieDic["6점미만"] +=1

#font
import matplotlib as mpl
import matplotlib.pyplot as plt

font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()
mpl.rc('font', family=font_name)

figure = plt.figure()
axes = figure.add_subplot(111)
axes.pie(movieDic.values(), labels=movieDic.keys(), autopct='%.1f%%')
plt.show()