import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
# 영화 : 앤트맨과 와스프: 퀀텀매니아 / 평점 : 7.2 / 애매률 : 47.1%

# 영화 : 네가 떨어뜨린 푸른 하늘 / 평점 : 7.6 / 예매률 : 0.1$

r = requests.get(url)
ht = r.text
so = BeautifulSoup(ht, 'html.parser')

# print('영화 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > strong > a').string,
# ' / 평점 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').string,
# ' / 예매률 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(1) > div > div.thumb_cont > span.txt_append > span:nth-child(2) > span').string)

# print('영화 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(20) > div > div.thumb_cont > strong > a').string,
# ' / 평점 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(20) > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').string,
# ' / 예매률 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child(20) > div > div.thumb_cont > span.txt_append > span:nth-child(2) > span').string)

# for i in range(1,20):
#     i=str(i)
#     print('영화 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child('+i+') > div > div.thumb_cont > strong > a').get_text(),
# ' / 평점 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child('+i+') > div > div.thumb_cont > span.txt_append > span:nth-child(1) > span').get_text(),
# ' / 예매률 : ',so.select_one('#mainContent > div > div.box_ranking > ol > li:nth-child('+i+') > div > div.thumb_cont > span.txt_append > span:nth-child(2) > span').get_text())

ol = so.select_one('#mainContent > div > div.box_ranking > ol')
lis = ol.select("li")
# print(lis)
for i in lis:
    movieTitle = i.select_one("a.link_txt").get_text()
    movieGrade = i.select_one("span.txt_grade").get_text()
    movieReser = i.select_one("span.txt_num").get_text()
    print('영화 : ', movieTitle, end=' /')
    print('평점 : ', movieGrade, end=' /')
    print('예매률 : ', movieReser)

print('----------------')
# find 사용
movies = []
for i in lis:
    movieTitle = i.find('a', class_='link_txt').get_text()
    movieGrade = i.find("span", 'txt_grade').get_text()
    movieReser = i.find("span", {'class': "txt_num"}).get_text()
    print('영화 : ', movieTitle, end=' /')
    print('평점 : ', movieGrade, end=' /')
    print('예매률 : ', movieReser)
    movies.append([movieTitle, movieGrade, movieReser])

movie_df = pd.DataFrame(movies, columns=('영화제목', '평점', '예매률'))
print(movie_df)
