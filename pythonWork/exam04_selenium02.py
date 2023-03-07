from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import matplotlib as mpl

path = "C:\pythonWork\chromedriver.exe"
options = wd.ChromeOptions()
# options.add_experimental_option('excludeSwitches',['enable-logging'])
options.add_experimental_option('detach', True)
driver = wd.Chrome(path, options=options)
# print(driver)
# driver.get('https://google.com')
r = driver.execute_script('return 100*50')
print(r)
