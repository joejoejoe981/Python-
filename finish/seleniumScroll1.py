from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.get("https://www.dcard.tw/f")
#將滾動條拖到最底部
js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(3)
#將滾動條拖到最頂部
js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(3)
driver.quit()
print("滾動成功")