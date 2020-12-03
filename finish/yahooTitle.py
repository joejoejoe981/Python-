# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import urllib.parse

r = requests.get("https://tw.yahoo.com")

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text,"html.parser")
    print(r.text)
    stories = soup.find_all('a',class_="story-title")
    for s in stories:
        print("標題:", s.text)
        print("網址:", urllib.parse.unquote(s.get('href')))