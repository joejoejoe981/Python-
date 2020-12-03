# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
import tkinter as tk 
import re

lottoUrl='https://www.taiwanlottery.com.tw/Lotto/Lotto649/history.aspx'

def hit_me():
    payLoad={
        '__EVENTTARGET':'',
        '__EVENTARGUMENT':'',
        '__LASTFOCUS':'',
        '__VIEWSTATE':VIEWSTATE,
        '__VIEWSTATEGENERATOR':VIEWSTATEGENERATOR,
        '__EVENTVALIDATION':EVENTVALIDATION,
        "Lotto649Control_history$chk": "radYM",
        "Lotto649Control_history$dropYear": yearText.get(),
        "Lotto649Control_history$dropMonth": monthText.get(),
        "Lotto649Control_history$btnSubmit": "查詢"}


    res = requests.post(lottoUrl, headers=headers, data=payLoad)
    
    soup = BeautifulSoup(res.text,'html.parser')   
    
    number = soup.find_all("span", id = re.compile("Lotto649Control_history_dlQuery_SNo\d_\d"))
    
    superNumber = soup.find_all("span", id = re.compile("SuperLotto638Control_history1_dlQuery_No7_\d"))

    i = 0
    j = 0
    output = ""

    for item in number:
        output = output + item.text+" "
        i = i + 1
        if i == 6:
            output = output + superNumber[j].text+ '\n'
            i = 0
            j = j + 1
    numberLable.configure(text=output)              

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
res = requests.get(lottoUrl, headers=headers)
soup = BeautifulSoup(res.text,'html.parser')

VIEWSTATE = soup.find(id = "__VIEWSTATE").get("value")
VIEWSTATEGENERATOR = soup.find(id = "__VIEWSTATEGENERATOR").get("value")
EVENTVALIDATION = soup.find(id = "__EVENTVALIDATION").get("value")        

window = tk.Tk()
window.title('My Window')
window.geometry('300x100')    
                            
yearLable = tk.Label(window,text='年')
yearLable.grid(row=0,column=0)

yearText = tk.Entry(window,width=10)
yearText.grid(row=0,column=1)

monthLable = tk.Label(window,text='月')
monthLable.grid(row=1,column=0)

monthText = tk.Entry(window,width=10)
monthText.grid(row=1,column=1)

numberLable = tk.Label(window)
numberLable.grid(row=2,column=0)

b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)
b.grid(row=3,column=0)
photo = tk.Label(window)
photo.grid(row=4,column=0)
 
window.mainloop() 