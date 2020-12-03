import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/wuzheyou/PycharmProjects/JOE/chromedriver')
driver.get('https://comicbus.com/html/18347.html')
time.sleep(2)
html = driver.page_source
print(html)
print('-----------------------')
time.sleep(3)
driver.quit()
