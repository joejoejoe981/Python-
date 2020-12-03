# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:07:41 2019

@author: Alvin
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('BROWSE TEMPLATES')
target.location_once_scrolled_into_view

sleep(3)
driver.quit()
print("滾動成功")