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

VIEWSTATE =soup.select_one("#__VIEWSTATE")["value"]
VIEWSTATEGENERATOR =soup.select_one("#__VIEWSTATEGENERATOR")["value"]
EVENTVALIDATION =soup.select_one("#__EVENTVALIDATION")["value"]                

payLoad={'__EVENTTARGET':'',
        '__EVENTARGUMENT':'',       
        '__VIEWSTATE':VIEWSTATE,
        '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
        '__EVENTVALIDATION':EVENTVALIDATION,
        'ctl00$header1$QueryTextBox':'',
        'ctl00$ContentPlaceHolder1$login1$IdTextBox':'',
        'ctl00$ContentPlaceHolder1$login1$PasswordTextBox':'',
        'ctl00$ContentPlaceHolder1$login1$OKButton': '登入'}
rs = requests.session()
res = rs.post(lccnetTV, headers=headers, data=payLoad)

Url2='https://www.lccnet.tv/userpages/mycard.aspx'

res = rs.get(Url2)
soup = BeautifulSoup(res.text,'html.parser')
resData = soup.find_all(class_='cardno')
resImg = soup.find_all(class_='box')
for i, j in zip(resData, resImg):
    print(i.text.strip()) 
    print(j.img.get('src')) 
    ImgUrl="https://www.lccnet.tv"+j.img.get('src')
    resp2 = requests.get(ImgUrl, headers=headers)
    if resp2.status_code == 200:    
        with open(i.text.strip()[3:]+".png", 'wb') as f:
                for chunk in resp2:
                    f.write(chunk)  
