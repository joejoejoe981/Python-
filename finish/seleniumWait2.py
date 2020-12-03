# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)  # 隱性等待，最長等30秒
driver.get('http://www.pchome.com.tw')

print(driver.current_url)
driver.quit()

