# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:26:37 2019

@author: user
"""

from selenium import webdriver#載入webdriver模組
from selenium.webdriver.common.keys import Keys 
import re
from bs4 import BeautifulSoup
product = 'apple'

browser=webdriver.Chrome()#建立瀏覽器物件
browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q="+product)
#print(browser.page_source)
for i in range(20):
    browser.find_element_by_tag_name('body').send_keys(Keys.END) 

soup = BeautifulSoup(browser.page_source, 'html.parser')

product = soup.find_all('h5')
productList=[]
for index, item in enumerate(product):
    #print("{0:2d}. {1}".format(index + 1, item.text.strip()))
    productList.append(item.text.strip())

price = soup.find_all('span',id=re.compile('price_.*'))
priceList=[]
for index, item in enumerate(price):
    #print("{0:2d}. {1}".format(index + 1, item.text.strip()))
    priceList.append(item.text.strip())

for i in range(len(priceList)):
    print("{0:2d}. {1} {2}".format(i + 1, productList[i], priceList[i]))
    

browser.quit()