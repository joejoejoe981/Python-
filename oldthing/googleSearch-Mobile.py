# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 20:19:07 2019

@author: ASUS
"""

import requests
from bs4 import BeautifulSoup
import urllib.parse

googleUrl = 'https://www.google.com.tw/search'

my_params={'q':'寒流'}

r = requests.get(googleUrl, params=my_params)

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text,"html.parser")
    #print(r.text)
    
    itemsTitle = soup.find_all('div',class_="BNeawe vvjwJb AP7Wnd")
    itemsLink = soup.select('div.kCrYT > a')
    
    for t,l in zip(itemsTitle,itemsLink):
        print("標題:",t.text)
        index = l.get("href").index('&sa')
        url = urllib.parse.unquote(l.get('href')[7:index])
        print("網址:",urllib.parse.unquote(url))      