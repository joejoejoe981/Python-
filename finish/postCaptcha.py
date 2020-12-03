# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests #引入函式庫
from bs4 import BeautifulSoup


url = 'https://www.post.gov.tw/post/internet/SearchZone/index.jsp?ID=130107'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
resp = requests.get(url, headers=headers)
#print(resp.text)

soup = BeautifulSoup(resp.text, 'html.parser')

picUrl=''
mobileImg = soup.find_all('img', id='imgCaptcha3')
for item in mobileImg:
    try:
        #print(item['src'][3:])
        picUrl=item['src'][3:]
    except:
        pass

resp2 = requests.get("https://www.post.gov.tw/post/internet/"+picUrl, headers=headers)
if resp2.status_code == 200:
    with open("test.jpg", 'wb') as f:
        for chunk in resp2:
            f.write(chunk)
  