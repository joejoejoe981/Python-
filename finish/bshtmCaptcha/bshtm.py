import requests
from bs4 import BeautifulSoup
import cv2
import numpy as np
import os
import time

def mse(imageA, imageB):
    err = np.sum((imageA.astype('float') - imageB.astype('float')) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def getNumber(pic):
    min_a = 9999999999
    min_jpg = None    
    for jpg in os.listdir('Alpabet_reference'):
        ref = cv2.imread('Alpabet_reference/' + jpg)
        if mse(ref, pic) < min_a:
            min_a = mse(ref, pic)
            min_jpg = jpg
    return min_jpg

def download_captcha():
    
    #把驗證碼下載下來
    bsMenu_Url = 'http://bsr.twse.com.tw/bshtm/bsMenu.aspx'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    
    res = requests.get(bsMenu_Url, headers = headers)
    res.encoding = 'utf-8'
    global soup
    soup = BeautifulSoup(res.text, 'html.parser')
    
    sel = soup.select('img')
    
    txt = sel[1]['src']
    captchaUrl = 'http://bsr.twse.com.tw/bshtm/' + txt
    
    resp = requests.get(captchaUrl, headers = headers)
    if resp.status_code == 200:
        with open("test.jpg", 'wb') as f:
            for chunk in resp:
                f.write(chunk)    
    
    ###   驗證碼影象處理    
    image = cv2.imread('test.jpg')
    
    kernel = np.ones((4,4), np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 1)
    blurred = cv2.GaussianBlur(erosion, (5,5), 0)
    edged = cv2.Canny(blurred, 30, 150)
    dilation = cv2.dilate(edged, kernel, iterations = 1)  
    
    #找出輪廓
    contours, hierarchy = cv2.findContours(dilation.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted([(c,cv2.boundingRect(c)[0] ) for c in contours], key = lambda x:x[1])
    ary = []
    for(c, _) in cnts:
        (x,y,w,h) = cv2.boundingRect(c)
        if w > 15 and h > 15:
            ary.append((x,y,w,h))
    
    #切割成五張圖
    for id, (x,y,w,h) in enumerate(ary):
        roi = dilation[y:y+h,x:x+w]
        thresh = roi.copy()
        res = cv2.resize(thresh, (50,50))
        cv2.imwrite('%d.jpg'%(id), res)
    
    pic_list = [cv2.imread('0.jpg'), cv2.imread('1.jpg'), cv2.imread('2.jpg'), cv2.imread('3.jpg') , cv2.imread('4.jpg')]
            
    solution = []
    for item in pic_list:
        it = str(getNumber(item)[0:1])
        solution.append(it)
    
    global answer
    answer = solution[0]+solution[1]+solution[2]+solution[3]+solution[4]    
    
def recognize_payLoad():

    global soup
    VIEWSTATE = soup.select_one("#__VIEWSTATE")["value"]
    EVENTVALIDATION = soup.select_one("#__EVENTVALIDATION")["value"]  
    
    # 開始登入
    global stock_number
    stock_number = stock
                                      
    payLoad = {'__EVENTTARGET':'',
               '__EVENTARGUMENT':'',
               '__LASTFOCUS':'',
               '__VIEWSTATE':VIEWSTATE,
               '__VIEWSTATEGENERATOR':'AA1F01CB',
               '__EVENTVALIDATION':EVENTVALIDATION,
               'RadioButton_Normal':'RadioButton_Normal',
               'TextBox_Stkno':stock_number,
               'CaptchaControl1':answer,
               'btnOK':'查詢'
               }
    
    global session
    session = requests.Session()
    
    url = 'https://bsr.twse.com.tw/bshtm/bsMenu.aspx'
    res = session.post(url, data = payLoad)
    res.encoding = 'utf-8-sig'
    soup1 = BeautifulSoup(res.text, 'html.parser')    
    sel = soup1.find_all(class_ = 'radio')

    global authenticate
    authenticate = sel[3].text    

def checking():
    if authenticate == '驗證碼錯誤!':
        print('重新載入中...')
        download_captcha()
        time.sleep(1)
        recognize_payLoad()
        checking()
        
    else:
        print('以下為證券代號{}的資料:'.format(stock_number))
        data_Url = 'http://bsr.twse.com.tw/bshtm/bsContent.aspx'
        resp = session.get(data_Url)
        if resp.status_code == 200:
            with open("data.csv", 'w', encoding = 'utf-8-sig') as f:
                f.write(resp.text)
        print(resp.text)
        
stock = input("請輸入號碼: ")

download_captcha()
recognize_payLoad()
checking()





