from bs4 import BeautifulSoup
html = """
    <html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
#여러줄의 문자열을 입력할때 """ """이나 ''' '''을 이용
# print(html)
soup = BeautifulSoup(html,'html.parser')
print(soup)
h1 = soup.html.body.h1
print(h1)
p = soup.html.body.p
print(p)
p1 = p.next_sibling.next_sibling
print(p1)
#####################
print('h1 string : ', h1.string)
print('h1 text : ', h1.text)
print('p : ', p.string)
print('p1 : ', p1.text)

html2 = """
    <html><body>
    <h1 id='title'>스크레이핑이란?</h1>
    <p id='body'>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
    </body></html>
"""
soup = BeautifulSoup(html2,'html.parser')
title = soup.find(id='title')
print(title.string)
# id=body 인 내용 추출
body = soup.find(id='body')
print(body.text)