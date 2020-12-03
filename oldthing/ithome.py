# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

for i in range(5):
    r = requests.get('https://www.ithome.com.tw/latest?page='+str(i))
    
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,'html.parser')
        data = soup.find_all('p', class_ = 'title')
        for i in data:
            print(i.text)
            print('https://www.ithome.com.tw'+i.a.get('href'))
