from selenium import webdriver as wd
from selenium.webdriver.common.by import By

path = "C:\pythonWork\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# print(driver)
driver.get('https://www.naver.com/')

driver.find_element(By.ID, 'query').send_keys('파이썬')
driver.find_element(By.ID, 'search_btn').click()
