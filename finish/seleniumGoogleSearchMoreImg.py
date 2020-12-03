import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep
import re

asq = 1
item = 'android'

url = 'https://www.google.com/search?q='+item+'&sxsrf=ACYBGNTCQHZ6xM5A3BprdxQPdAYCuTgLwg:1576477254796&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi8zZK2w7nmAhVjHKYKHRjMC6UQ_AUoAXoECBAQAw&biw=1536&bih=758#imgrc=_'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
'x-client-data': 'CJS2yQEIpbbJAQjEtskBCKmdygEIvLDKAQjnscoBCPe0ygEYq6TKAQ=='}

driver = webdriver.Chrome()
driver.get(url)
for i in range(2):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    sleep(1)
    
soup = BeautifulSoup(driver.page_source,'html.parser')
driver.quit()

f= soup.find_all("img",class_="rg_i Q4LuWd tx8vtf")
for i in f:
    try:        
        pic = requests.get(i.get('data-src'),headers = header)
        if pic.status_code == 200:
           asq +=1
           with open(str(asq) + ".jpg", 'wb') as f:
                for chunk in pic:
                     f.write(chunk)
                #print('GetIT')        
    except:
        pass
print('ok')