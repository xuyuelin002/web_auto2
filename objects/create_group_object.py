#!/usr/bin/env python
# encoding: utf-8
'''
@author: xuyuelin
@file: test_create_group.py
@time: 2022/4/1 10:13
@desc:
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CreateGroupPage:
    def __init__(self,driver):
        self.driver=driver
        self.choose_elem=By.ID,'group_type'
        self.text_elem = By.XPATH, '/html[1]/body[1]/div[4]/div[1]/dl[1]/dt[1]/a[1]'
    def inkey(self, group_type):
        select = self.driver.find_element(*self.choose_elem)
        Select(select).select_by_visible_text(group_type)
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text