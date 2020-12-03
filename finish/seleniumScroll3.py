# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:00:23 2019

@author: Alvin
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.w3schools.com/')
target = driver.find_element_by_link_text('BROWSE TEMPLATES')
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
sleep(3)
driver.quit()
print("滾動成功")