
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/wuzheyou/PycharmProjects/JOE/chromedriver')
driver.get('https://invest.cnyes.com/twstock/tws/2330/history')
time.sleep(2)
html = driver.page_source
print(html)
print('-----------------------------------------------------')

picker_btn = driver.find_element_by_xpath('//*[@id="_historyDataTable"]/div[2]/div[1]/div/button/span')
picker_btn.click()
time.sleep(2)
start_date = driver.find_element_by_xpath()
