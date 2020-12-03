# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests #引入函式庫
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract

while True:
    postUrl = 'https://www.post.gov.tw/post/internet/SearchZone/index.jsp?ID=130107'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    rs = requests.session()
    resp = rs.get(postUrl, headers=headers)
    #print(resp.text)
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    picUrl=''
    mobileImg = soup.find_all('img', id='imgCaptcha3_zip6')
    for item in mobileImg:
        try:
            #print(item['src'][3:])
            picUrl=item['src'][3:]
        except:
            pass
    
    resp2 = rs.get("https://www.post.gov.tw/post/internet/"+picUrl, headers=headers)
    if resp2.status_code == 200:
        with open("test.jpg", 'wb') as f:
            for chunk in resp2:
                f.write(chunk)
                
    pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    img = Image.open('test.jpg')
    img = img.convert('L')
    ans = pytesseract.image_to_string(img, config ='--psm 6')
    #print(ans)            
    
    vKey = soup.find('input', {'name': 'vKey'}).get('value')
    
    payLoad={'list': '5',
             'list_type': '1',
             'firstView': '3',
             'vKey': vKey,
             'city_zip6': '臺北市',
             'cityarea_zip6': '中正區',
             'street_zip6': '三元街',
             'checkImange_zip6': ans,
             'Submit': '查詢'}
    
    resp3 = rs.post(postUrl, data=payLoad, headers=headers)
    if "驗證碼輸入錯誤" in resp3.text:
        print("驗證碼錯誤，重新下載比對")
    else:
        soup2 = BeautifulSoup(resp3.text,'html.parser') 
        table = soup2.find_all(attrs={'data-th':'郵遞區號'})
        table2 = soup2.find_all(attrs={'data-th':'投遞範圍'})
    
        for zipCode, zipRegion in zip(table, table2):
            print(zipCode.text,zipRegion.text)
        break
