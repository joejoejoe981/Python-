# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 10:00:04 2019

@author: ASUS
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
url = ['https://shopping.pchome.com.tw/',
       'https://tw.buy.yahoo.com/?co_servername=sME&c2=sME',
       'https://www.momoshop.com.tw/main/Main.jsp?mdiv=1099800000-bt_0_243_01-bt_0_243_01_e1&ctype=B'
       ]

'''
options = webdriver.ChromeOptions()
options.add_argument('--headless')#隱藏瀏覽器畫面,上傳雲端必備
browser=webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
'''

browser = webdriver.Chrome()
word = '洗衣機'
All_data=[]

print('Pchome商品')
print('-------------------------------------------------')
browser.get(url[0])
keyword=browser.find_element_by_id('keyword')
keyword.send_keys(word)
botton = browser.find_element_by_id('doSearch')
botton.click()

WebDriverWait(browser,10).until(
        expected_conditions.presence_of_element_located((By.ID,'ItemContainer')))

soup = BeautifulSoup(browser.page_source,'html.parser')
select_title = soup.select('h5')
while len(select_title) < 100:
    html=browser.find_element_by_tag_name('html')
    html.send_keys(Keys.END)
    soup = BeautifulSoup(browser.page_source,'html.parser')
    select_title = soup.select('h5')

select_url = soup.select('h5 > a')
select_price = soup.find_all('span', class_='price')

index=1
for i,j,k in zip(select_title,select_url,select_price):
    print(index, i.text, k.text)
    #print(i.text, j.get('href'), k.text)
    index+=1
    #All_data.append([i.text, j.get('href'), k.text])
    

print('-------------------------------------------------\n')

print('Yahoo商品')
print('-------------------------------------------------')
browser.get(url[1])
keyword=browser.find_element_by_css_selector('input')
keyword.send_keys(word)
botton = browser.find_element_by_link_text('搜尋商品')
botton.click()

WebDriverWait(browser,10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME,'pageFlex')))

soup = BeautifulSoup(browser.page_source,'html.parser')
select_title = soup.find_all(class_='BaseGridItem__title___2HWui')
select_url = soup.find_all(class_='BaseGridItem__content___3LORP BaseGridItem__hover___3UlCS')
select_price = soup.find_all(class_='BaseGridItem__price___31jkj')

index=1
for i,j,k in zip(select_title,select_url,select_price):
    print(index, i.text, k.text)
    #print(index, i.text,j.get('href'),k.text)
    index+=1
    #All_data.append([i.text, j.get('href'), k.text])


print('-------------------------------------------------\n')

print('momo商品')
print('-------------------------------------------------')
browser.get(url[2])
keyword=browser.find_element_by_id('keyword')
keyword.send_keys(word)
botton = browser.find_element_by_class_name('inputbtn')
botton.click()

WebDriverWait(browser,10).until(
        expected_conditions.presence_of_element_located((By.CLASS_NAME,'searchPrdListArea.bookList')))

soup = BeautifulSoup(browser.page_source,'html.parser')
select_title = soup.find_all(class_='prdName')
select_url = soup.find_all(class_='goodsUrl')
select_price = soup.find_all(class_='price')
index=1
for i,j,k in zip(select_title,select_url,select_price):
    print(index, i.text, k.text)
    #print(index,i.text, 'https://www.momoshop.com.tw/' + j.get('href'), k.text)
    index+=1
    #All_data.append([i.text, 'https://www.momoshop.com.tw/' + j.get('href'), k.text])
    
'''
for i in range(len(All_data)):
    print(str(i+1)+'.'+','.join(All_data[i]))
'''
print('-------------------------------------------------')
browser.close()