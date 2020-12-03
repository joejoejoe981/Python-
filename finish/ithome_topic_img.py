# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

title = []
url = []
imageUrl = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

for i in range(5):
    r = requests.get('https://www.ithome.com.tw/latest?page='+str(i), headers=headers)
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'html.parser')
        
        data = soup.find_all('p', class_ = 'title')
        for i in data:
            title.append(i.text)
            url.append('https://www.ithome.com.tw'+i.a.get('href'))
        
        data = soup.find_all('p', class_ = 'photo')

        for i in data:
            temp = str(i.img)
            findex = temp.find('src')
            temp2 = temp[findex+5:]
            lindex = temp2.find('"')
            imageUrl.append(temp2[:lindex])
            
for tt, url in zip(title, imageUrl):
    try:
        resp2 = requests.get(url, headers=headers)
        if resp2.status_code == 200:
            chars = '/\\`*_{}[]()<>#+-.!$?:'
            for c in chars:
                tt = tt.replace(c, '')
            with open(tt+'.jpg', 'wb') as f:
                for chunk in resp2:
                    f.write(chunk)             
    except:
        pass
