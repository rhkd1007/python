from bs4 import BeautifulSoup

fp = open('fruits-vegetables.html', encoding='utf-8')
# print(fp)
soup = BeautifulSoup(fp, 'html.parser')
# print(soup)

# print(soup.select_one("li:nth-of-type(6)").string) # 파프리카 # version 이슈로 사용 불가
print(soup.select_one("#ve-list > li[data-lo='us']").string) # 파프리카
print(soup.select("#ve-list > li[data-lo='us']")[0].string) # 파프리카
print(soup.select("#ve-list > li[data-lo='us']")[1].string) # 아보카도
# 아보카도
print(soup.select_one("#ve-list > li.black").string) # 가지
print('-------------')
print(soup.select_one("#ve-list > li:nth-of-type(4)").string) # 아보카도

conditon = {'data-lo' : 'us', 'class' : 'black'}
print(soup.find("li",conditon).string) # 아보카도
print(soup.find(id="ve-list").find("li", conditon).string)# 아보카도

