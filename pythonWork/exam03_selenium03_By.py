import time
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

path = "C:\pythonWork\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# print(driver)
driver.get('https://www.youtube.com/c/paikscuisine/videos')
# page = driver.page_source

# all_videos = driver.find_elements(By.ID, "dismissible")
all_videos = driver.find_elements(By.CSS_SELECTOR, "#dismissible")
print(all_videos)

time.sleep(2)
# 제목, 재생시간, 조회수
datas = []
for video in all_videos:
    title = video.find_element(By.ID, 'video-title').text
    video_time = video.find_element(By.CSS_SELECTOR, '.style-scope ytd-thumbnail-overlay-time-status-renderer').text.strip()
    # //*[@id="metadata-line"]/span[1]
    video_num = video.find_element(By.XPATH, '//*[@id="metadata-line"]/span[1]').text.strip()
    datas.append([title,video_time,video_num])

print(datas)




# title = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
# print(title)

# driver.find_element(By.ID, 'query').send_keys('파이썬')
# driver.find_element(By.ID, 'search_btn').click()

# page = driver.page_source

# #metadata-line > span:nth-child(3)
# #metadata-line > span:nth-child(3)

# soup = BeautifulSoup(page, 'html.parser')

# all_videos = soup.find_all(id='dismissible')
# datas =[]

# # 제목, 재생시간, 조회수
# for video in all_videos:
#     title = video.find(id='video-title').text #제목
#     video_time = video.find('span',{'class' : 'style-scope ytd-thumbnail-overlay-time-status-renderer'}).text.strip() #재생시간
#     video_num = video.find('span',{'class' : 'inline-metadata-item style-scope ytd-video-meta-block'}).text.strip() # 조회수
#     datas.append([title, video_time, video_num])
# print(datas)

# import pandas as pd
# df = pd.DataFrame(datas, columns=('제목', '재생시간', '조회수'))
# df.to_csv('youtubu.csv', encoding='utf-8-sig', index=True)

# # 유튜브 조회수 34만회

# youtubu_dic = {'100만이상': 0, '50만이상': 0, '10만이상': 0}
# for item in datas:
#     item = float(str(item).split('조회수')[1].split('만회')[0].strip())
#     if item >= 100 :
#         youtubu_dic['100만이상'] +=1
#     elif item >= 50 :
#         youtubu_dic['50만이상'] +=1
#     elif item >= 10 :
#         youtubu_dic['10만이상'] +=1
# print(youtubu_dic)

# # 그래프 그리기
# # 한글
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# font_name = mpl.font_manager.FontProperties(
#     fname='c:/Windows/fonts/malgun.ttf').get_name()
# mpl.rc('font', family=font_name)

# figure = plt.figure()
# axes = figure.add_subplot(111)
# axes.pie(youtubu_dic.values(), labels=youtubu_dic.keys(), autopct='%.1f%%')
# plt.show()
