# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.pchome.com.tw')

sleep(3)  # 強制等待3秒再執行下一步

print(driver.current_url)
driver.quit()

