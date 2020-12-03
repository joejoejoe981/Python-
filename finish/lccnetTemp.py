# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
     
lccnetTV='https://www.lccnet.tv/pages/login.aspx'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

res = requests.get(lccnetTV, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

VIEWSTATE =''
VIEWSTATEGENERATOR =''
EVENTVALIDATION =  ''          

payLoad={
        }

rs = requests.session()
res = rs.post(lccnetTV, headers=headers, data=payLoad)

Url2='https://www.lccnet.tv/userpages/mycard.aspx'

res = rs.get(Url2)
