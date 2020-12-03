import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/wuzheyou/PycharmProjects/JOE/chromedriver')
driver.get('https://www.google.com.tw/')
time.sleep(6)
search_box = driver.find_element_by_name('q')
search_box.send_keys('python')
time.sleep(6)
driver.quit()