# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:05:50 2019

@author: Alvin
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('BROWSE TEMPLATES')
driver.execute_script('arguments[0].scrollIntoView(true);', target)
sleep(3)
driver.quit()
print("滾動成功")