# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 10:16:42 2019

@author: ASUS
"""

from bs4 import BeautifulSoup
import requests
from datetime import date

today   = date.today()
dateDate=(str(today)).split("-")
year    = dateDate[0]
month   = str(int(dateDate[1]))
day     = int(dateDate[2])

def ptt(keyword, before):
    itemTitleList = []
    itemLinkList = []
    itemDateList = []    
    pttUrl='https://www.ptt.cc/ask/over18'

    payLoad={'from': '/bbs/Gossiping/index.html',
             'yes': 'yes'}
    
    rss = requests.session()
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    rss.post(pttUrl, data=payLoad, headers = headers)
    
    url = "https://www.ptt.cc/bbs/Gossiping/index.html"  
    dateScope=[day-before, day] 
    
    while True: 
        res = rss.get(url)
        if res.status_code == requests.codes.ok:
            soup = BeautifulSoup(res.text,"html.parser")            
            itemDate = soup.select('div.r-ent > div.meta > div.date')
            itemTitle = soup.select('div.r-ent > div.title > a')
            itemLink = soup.select('div.r-ent > div.title > a')
            u = soup.select("div.btn-group.btn-group-paging a") #a標籤
            url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址    
            
            for d, title, link in zip(itemDate, itemTitle, itemLink):
                for i in range(dateScope[1],dateScope[0],-1):   
                    if d.text.strip() == month+'/'+str(dateScope[0]):
                        print("--------------------------------------------")
                        print("已經都抓完囉")
                        return
                    if d.text.strip() == month+'/'+str(i) and keyword in title.text and 'Re:' not in title.text:
                        print(title.text, d.text.strip())
                        itemTitleList.append(title.text)
                        itemLinkList.append(link.get('href'))
                        itemDateList.append(d.text.strip()) 

while True:
    keyword = input("請輸入想搜尋的新聞關鍵字(或按q結束程式):")
    if keyword=="q" or keyword=="Q":
        print("結束程式")
        break
    else:
        before = eval(input("請輸入想搜尋幾天的新聞:"))
        ptt(keyword,before) 
    
     