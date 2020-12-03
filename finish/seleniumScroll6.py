from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
# Use send_keys(Keys.HOME) to scroll up to the top of page
driver.find_element_by_tag_name('body').send_keys(Keys.END) 

sleep(3)
driver.quit()
print("滾動成功")

