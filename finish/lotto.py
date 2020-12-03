# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
resp = requests.get(url, headers=headers)

soup = BeautifulSoup(resp.text, 'html.parser')
__VIEWSTATE = soup.find(id = "__VIEWSTATE").get("value")
__VIEWSTATEGENERATOR = soup.find(id = "__VIEWSTATEGENERATOR").get("value")
__EVENTVALIDATION = soup.find(id = "__EVENTVALIDATION").get("value")

for year in range(103,110):
    for month in range(1,13):
        searchData = {"__EVENTTARGET":"",
                      "__EVENTARGUMENT":"",
                      "__LASTFOCUS":"",
                      "__VIEWSTATE":__VIEWSTATE,
                      "__VIEWSTATEGENERATOR":__VIEWSTATEGENERATOR,
                      "__EVENTVALIDATION":__EVENTVALIDATION,
                      "SuperLotto638Control_history1$DropDownList1": "1",
                      "SuperLotto638Control_history1$chk": "radYM",
                      "SuperLotto638Control_history1$dropYear": year,
                      "SuperLotto638Control_history1$dropMonth": month,
                      "SuperLotto638Control_history1$btnSubmit": "查詢"
        }
        
        resp = requests.post(url, headers=headers, data=searchData)
        
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        value = soup.find_all(id = re.compile("SuperLotto638Control_history1_dlQuery_SNo\d_\d"))
        count = 0
        for i in value:
            print(i.text,end=' ')
            count=count+1
            if count % 7 == 0:
                print('')
            
