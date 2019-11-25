#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 23:38:44 2019

@author: devastator
"""

from selenium import webdriver 

browser=webdriver.Chrome('./chromedriver')
browser.maximize_window()
browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in browser.title


''' button=browser.find_element_by_class_name("btn-default")
print(button.get_attribute('innerHTML'))

assert 'Show Message' in browser.page_source '''

field=browser.find_element_by_id("user-message")
field.clear()
field.send_keys("Text")

button=browser.find_element_by_class_name("btn-default")
button.click()

