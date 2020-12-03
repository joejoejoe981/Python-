from selenium import webdriver
driver = webdriver.PhantomJS(executable_path=r'phantomjs')  # PhantomJs
driver.get('http://pala.tw/js-example/')  # 輸入範例網址，交給瀏覽器 
pageSource = driver.page_source  # 取得網頁原始碼
print(pageSource)
driver.close()  # 關閉瀏覽器
