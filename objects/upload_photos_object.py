#!/usr/bin/env python
# encoding: utf-8
'''
@author: xuyuelin
@file: test_upload_photos.py
@time: 2022/4/1 10:12
@desc:
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class UploadPage:
    def __init__(self,driver):
        self.driver=driver
        self.choose_elem=By.ID,'album_name'
        self.text_elem = By.XPATH, '/html[1]/body[1]/div[4]/dl[1]/dt[1]/a[1]/img[1]'
    def inkey(self,album_name):
        select = self.driver.find_element(*self.choose_elem)
        Select(select).select_by_visible_text(album_name)
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text