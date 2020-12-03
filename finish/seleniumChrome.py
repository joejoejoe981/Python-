# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:42:23 2019

@author: cadtc
"""

from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://pala.tw/js-example/')    #輸入範例網址，交給瀏覽器 
pageSource = driver.page_source             #取得網頁原始碼
print(pageSource)
driver.close()  #關閉瀏覽器
