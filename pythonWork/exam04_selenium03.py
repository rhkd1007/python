import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

path = "C:\pythonWork\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# print(driver)
driver.get('https://www.youtube.com/c/paikscuisine/videos')

# all_videos = driver.find_elements(By.ID, "dismissible")
all_videos = driver.find_elements(By.CSS_SELECTOR, "#dismissible")

body_tag = driver.find_element(By.TAG_NAME, 'body')
print(body_tag)
# 스크롤이 1번 진행된다.
body_tag.send_keys(Keys.END)

# 길이 확인하기
# document.documentElement.scrollHeight
print(driver.execute_script('return document.documentElement.scrollHeight'))

while True:
    last_height = driver.execute_script(
        'return document.documentElement.scrollHeight')
    print('last_height : ', last_height)
    # 10번 스크롤하기
    for i in range(10):
        body_tag.send_keys(Keys.END)
        time.sleep(1)
        new_heiget = driver.execute_script(
            'return document.documentElement.scrollHeight')
        print('new_heiget : ', new_heiget)

    if last_height == new_heiget:
        print('화면길이 같아서 반복 종료')
        break
