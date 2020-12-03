from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

url ='https://tw.yahoo.com/'

#可以不讓瀏覽器執行在前景，而是在背景執行, 如以下宣告 options
ChromeOptions = webdriver.ChromeOptions()
ChromeOptions.add_argument('--headless')

#打開瀏覽器,然後將options加入Chrome方法裡面
browser=webdriver.Chrome(options=ChromeOptions)
#在瀏覽器打上網址連入
browser.get(url) 

#這時候就可以分析網頁裡面的元素
element = browser.find_element_by_id('UHSearchBox')
element.send_keys('Hello World')

sumbit = browser.find_element_by_id('UHSearchWeb').click()

# 等待目標表格'id 為 web'的div出現
element = WebDriverWait(browser, 5).until(
    expected_conditions.presence_of_element_located((By.ID, 'web'))
)

#然後就是beautifulsoup的範疇了，將browser.page_source放進去分析
soup=BeautifulSoup(browser.page_source,"html.parser")
links = soup.select('div#web h3')

for link in links:
    print(link.text)

browser.quit()