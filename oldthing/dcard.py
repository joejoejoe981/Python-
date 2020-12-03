# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.dcard.tw/f')

if r.status_code == 200:
    soup = BeautifulSoup(r.text,'html.parser')
    data = soup.find_all('a', class_ = 'sc-1v1d5rx-4')
    for i in data:
            print(i.string)
            print('https://www.dcard.tw'+i.get('href'))
