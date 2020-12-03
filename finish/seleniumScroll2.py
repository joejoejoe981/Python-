from selenium import webdriver  
import time  

driver=webdriver.Chrome()  
driver.get("http://www.baidu.com")  
#搜尋  
driver.find_element_by_id("kw").send_keys("selenium")  
driver.find_element_by_id("su").click()  
time.sleep(3)  

#將頁面滾動條拖到底部  
js="var q=document.documentElement.scrollTop=10000"  
driver.execute_script(js)  
time.sleep(3)  

#將滾動條移動到頁面的頂部  
js="var q=document.documentElement.scrollTop=0"  
driver.execute_script(js)  
time.sleep(3)  

#將頁面滾動條移動到頁面任意位置，改變等於號後的數值即可  
js="var q=document.documentElement.scrollTop=50"  
driver.execute_script(js)  
time.sleep(10) 
driver.quit()
print("滾動成功")