# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

title=[]
imageUrl=[]
url = 'https://www.mobile01.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
resp = requests.get(url, headers=headers)


soup = BeautifulSoup(resp.text, 'html.parser')


mobile_title = soup.find_all('div',class_=['o-mainCardDesc','l-articleCardDesc'])
for item in mobile_title:
    title.append(item.text.strip())
   
mobile_img = soup.find_all(['span','img'],class_='lazy')
for item in mobile_img:
    imageUrl.append(item.get('data-src'))


for tt, url in zip(title, imageUrl):
    if 'https:' not in url:
        url = 'https:'+ url    
    resp2 = requests.get(url, headers=headers)
    if resp2.status_code == 200:
        chars = "/\\`*_{}[]()<>#+-.!$?:"
        for c in chars:
            tt = tt.replace(c, '')
        with open(tt+url[-4:], 'wb') as f:
            for chunk in resp2:
                f.write(chunk)  

