# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 10:26:37 2019

@author: user
"""

from selenium import webdriver#載入webdriver模組
import re
from bs4 import BeautifulSoup
import urllib.parse
productName = 'htc u12'

print('Pchome商品')
browser=webdriver.Chrome()#建立瀏覽器物件
browser.get("https://ecshweb.pchome.com.tw/search/v3.3/?q="+productName)
#print(browser.page_source)

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

print('---------------------------------------------------')

print('蝦皮商品')
browser=webdriver.Chrome()#建立瀏覽器物件
browser.get("https://shopee.tw/search?keyword="+productName)
#print(browser.page_source)

soup = BeautifulSoup(browser.page_source, 'html.parser')

product2 = soup.find_all('div',class_='_1NoI8_')
price2 = soup.find_all('span',class_='_341bF0')
productList2=[]
priceList2=[]
for item,price in zip(product2,price2):
    if(str.upper(productName) in item.text):
        productList2.append(item.text.strip())
        priceList2.append(price.text.strip())

for i in range(len(priceList2)):
    print("{0:2d}. {1} {2}".format(i + 1, productList2[i], priceList2[i]))

browser.quit()

print('---------------------------------------------------')

print('樂天商品')
browser=webdriver.Chrome()#建立瀏覽器物件
browser.get("https://www.rakuten.com.tw/search/"+productName+"/")
#print(browser.page_source)

data = re.sub('[\[CDATA\]]', '', browser.page_source)

indexStart = [m.start() for m in re.finditer('"prod_name"', data)]
indexEnd = [n.start() for n in re.finditer('"prod_uid"', data)]

data2 = data[data.index('id="ratPrice" value="'):]
data3 = data2[21:(data2.index('>')-1)] 

price = data3.split(',')
#print(price)

index=1
for i in range(20):
    print(index,":",urllib.parse.unquote(data[indexStart[i]+13:indexEnd[i]-2]),price[i])
    index = index+1

browser.quit()