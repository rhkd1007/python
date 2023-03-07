import requests
from bs4 import BeautifulSoup
import pandas as pd


url ='https://www.hollys.co.kr/store/korea/korStore.do'
r = requests.get(url)
ht = r.text
so = BeautifulSoup(ht,'html.parser')

#지역, 매장명, 주소, 전화번호
#contents > div.content > fieldset > div.tableType01 > table > tbody
#contents > div.content > fieldset > div.tableType01 > table > tbody > tr:nth-child(1)
#contents > div.content > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td.noline.center_t
#contents > div.content > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
#contents > div.content > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td:nth-child(4) > a
#contents > div.content > fieldset > div.tableType01 > table > tbody > tr:nth-child(2)


# print(so.select_one('#contents > div.content > fieldset > div.tableType01 > table > tbody > tr:nth-child(1) > td.noline.center_t'))

# tbody = so.select_one('#contents > div.content > fieldset > div.tableType01 > table > tbody')
# list = tbody.select("tr")
# for i in list:
#     city = i.select_one("td.noline.center_t")
#     chain = i.select("td.center_t > a"[1])
#     print(city)
#     print(chain)
# # print(list)
# ↑미완성

#contents > div.content > fieldset > div.tableType01 > table > tbody
tag_tbody = so.select_one("tbody")
# print(tag_tbody)
coffee_store = []
for store in tag_tbody.select('tr'):
    store_td = store.select('td')
    store_sido = store_td[0].string
    store_name = store_td[1].string
    store_address = store_td[3].string
    store_phone = store_td[5].string
    coffee_store.append([store_sido,store_name,store_address,store_phone])
print(coffee_store)

hollys_df = pd.DataFrame(coffee_store, columns=('지역','매장','주소','전화번호'))
print(hollys_df)

print('===================================')

coffee_store2 = []
for page in range(1,6):
    url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
    r = requests.get(url)
    ht = r.text
    so = BeautifulSoup(ht,'html.parser')
    #contents > div.content > fieldset > div.tableType01 > table > tbody
    tag_tbody = so.select_one("tbody")
    # print(tag_tbody)   
    for store in tag_tbody.select('tr'): 
        store_td = store.select('td')
        store_sido = store_td[0].string
        store_name = store_td[1].string
        store_address = store_td[3].string
        store_phone = store_td[-1].string
        coffee_store2.append([store_sido,store_name,store_address,store_phone])
print(coffee_store2)
print('-------------------------------------')

hollys_df2 = pd.DataFrame(coffee_store2, columns=('지역','매장','주소','전화번호'))
print(hollys_df2)

#https://www.hollys.co.kr/store/korea/korStore.do?pageNo=1&sido=&gugun=&store=

##########################
print('*'*20)
def hollys_store(result):
    for page in range(1,6):
        url = 'https://www.hollys.co.kr/store/korea/korStore.do?pageNo=%d&sido=&gugun=&store=' %page
        r = requests.get(url)
        ht = r.text
        so = BeautifulSoup(ht,'html.parser')
        #contents > div.content > fieldset > div.tableType01 > table > tbody
        tag_tbody = so.select_one("tbody")
        # print(tag_tbody)   
        for store in tag_tbody.select('tr'): 
            store_td = store.select('td')
            store_sido = store_td[0].string
            store_name = store_td[1].string
            store_address = store_td[3].string
            store_phone = store_td[-1].string
            result.append([store_sido,store_name,store_address,store_phone])
            
    return result

result = []
print('---Hollys store crawling >>>>>>>>>>>>>>>>>')
hollys_store(result)
print(result)

result_df = pd.DataFrame(coffee_store2, columns=('area','store','address','phone'))
print(result_df)