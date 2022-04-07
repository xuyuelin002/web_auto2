#!/usr/bin/env python
# encoding: utf-8
'''
@author: xuyuelin
@file: test_add_classification.py
@time: 2022/4/1 10:08
@desc:
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddClassificationPage:
    def __init__(self,driver):
        self.driver = driver
        self.text_elem = By.XPATH, '/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/select[1]'
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text