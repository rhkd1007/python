import bs4
import urllib.request
import pandas as pd

## 함수 선언부
def getBookInfo(book_tag) :
    names = book_tag.find("div", {"class": "goods_name"})
    bookName = names.find("a").text
    auths = book_tag.find("span", {"class": "goods_auth"})
    bookAuth = auths.find("a").text
    bookPub = book_tag.find("span", {"class": "goods_pub"}).text
    bookDate = book_tag.find("span", {"class": "goods_date"}).text
    bookPrice = book_tag.find("em", {"class": "yes_b"}).text
    return [bookName, bookAuth, bookPub, bookDate, bookPrice]

## 전역 변수부
url = "http://www.yes24.com/24/Category/Display/001001046001?ParamSortTp=05&PageNumber="
pageNumber = 1

## 메인 코드부
# while True :
#     try :
#         bookUrl = url + str(pageNumber)
#         pageNumber += 1

#         htmlObject = urllib.request.urlopen(bookUrl)
#         webPage = htmlObject.read()
#         bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
#         tag = bsObject.find('ul', {'class': 'clearfix'})
#         all_books = tag.findAll('div', {'class': 'goods_info'})

#         for book in all_books:
#             print(getBookInfo(book))

#     except :
#         break

# 1번 페이지만 데이터를 크롤링해서 제목, 저자, 출판사, 출판일, 가격
# with open
# yes24.csv 파일로 저장
# 그 파일을 읽어서 출력

one = []
while pageNumber==1 :
    try :
        bookUrl = url + str(pageNumber)
        pageNumber += 1

        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag = bsObject.find('ul', {'class': 'clearfix'})
        all_books = tag.findAll('div', {'class': 'goods_info'})

        for book in all_books:
            one.append(getBookInfo(book))          

    except :
        break

# print(one)

with open('yes24.csv','w',encoding='utf-8-sig') as f:
    f.write('제목  저자  출판사  발간일  가격\n')
    for item in one:
        row = ','.join(item)
        f.write(row+"\n")

######################
# 50번페이지까지
# yes24_50.csv 파일로 저장
# pandas
# 그 파일을 읽어서 출력

ff = []
while pageNumber<52 :
    try :
        bookUrl = url + str(pageNumber)
        pageNumber += 1

        htmlObject = urllib.request.urlopen(bookUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag = bsObject.find('ul', {'class': 'clearfix'})
        all_books = tag.findAll('div', {'class': 'goods_info'})

        for book in all_books:
            ff.append(getBookInfo(book))          

    except :
        break
# print(ff)

df = pd.DataFrame(ff,columns=('제목',  '저자',  '출판사',  '발간일',  '가격'))
df.to_csv('yes24_50.csv', encoding='utf-8-sig')