from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

path = "C:\pythonWork\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# print(driver)
driver.get('https://tour.interpark.com/?mbn=tour&mln=tour')

driver.find_element(By.ID, 'spHeaderInput').click()
driver.find_element(By.ID, 'txtHeaderInput').send_keys('제주도')
driver.find_element(By.ID, 'btnHeaderInput').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[2]/div/ul/li[2]').click()


#boxList > li:nth-child(1) > div > div.productInfo > div:nth-child(2) > div:nth-child(1) > a > h5
#boxList > li:nth-child(2) > div > div.productInfo > div:nth-child(2) > div:nth-child(1) > a > h5

#app > div > div:nth-child(1) > div.resultAtc > div.sortTabZone > div > ul > li:nth-child(1)
# //*[@id="app"]/div/div[1]/div[2]/div[2]/div/ul/li[1]
#app > div > div:nth-child(1) > div.resultAtc > div.sortTabZone > div > ul > li:nth-child(2)
# //*[@id="app"]/div/div[1]/div[2]/div[2]/div/ul/li[2]

time.sleep(2)
List = driver.find_elements(By.CLASS_NAME, "boxProduct")
# print(List)

names = []
for i in List:
    name = i.find_element(By.CLASS_NAME , 'infoTitle').text
    # grade = i.find_element(By.XPATH, '//*[@id="boxList"]/li[10]/div/div[2]/div[3]/div[2]/p[1]').text
    # print(grade)
    # print(name)
    names.append(name)
    # time.sleep(2)
    # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div[3]/div[2]/div[3]/button[2]').click()

    if name == '':
        del names[-1]
        break
names = set(names)
print(names)

# //*[@id="boxList"]/li[10]/div/div[2]/div[3]/div[1]/p
# //*[@id="boxList"]/li[1]/div/div[2]/div[3]/div[2]/p[1]
# //*[@id="boxList"]/li[10]/div/div[2]/div[3]/div[2]/p[1]