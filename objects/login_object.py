#!/usr/bin/env python
# coding:utf-8
'''
@author: xuyuelin
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.user_elem=By.ID, 'login_email'
        self.pass_elem=By.ID, 'login_pws'
        self.ck_login_elem=By.ID, 'loginsubm'
        self.exit_elem=By.LINK_TEXT, '退出'
        self.mypage_elem=By.LINK_TEXT,'我的主页'
    def user_paswd(self,username,password):
        self.driver.find_element(*self.user_elem).clear()
        self.driver.find_element(*self.user_elem).send_keys(username)
        self.driver.find_element(*self.pass_elem).clear()
        self.driver.find_element(*self.pass_elem).send_keys(password)
        self.driver.find_element(*self.ck_login_elem).click()
    def exit(self):
        self.driver.find_element(*self.exit_elem).click()

    def get_text(self):
        return self.driver.find_element(*self.mypage_elem).text

class CreateLogPage:
    def __init__(self,driver):
        self.driver = driver
        self.text_elem = By.XPATH, '/html[1]/body[1]/dl[1]/dt[1]/strong[1]/a[1]'
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

class AddClassificationPage:
    def __init__(self,driver):
        self.driver = driver
        self.text_elem = By.XPATH, '/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/select[1]'
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

class EditClassificationPage:
    def __init__(self,driver):
        self.driver = driver
        self.text_elem = By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]'
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

class CreateAlbumPage:
    def __init__(self,driver):
        self.driver = driver
        self.text_elem = By.XPATH, '/html[1]/body[1]/div[4]/dl[1]/dd[1]/strong[1]/a[1]'
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

class UploadPage:
    def __init__(self,driver):
        self.driver=driver
        self.choose_elem=By.ID,'album_name'
        self.text_elem = By.XPATH, '/html[1]/body[1]/div[4]/dl[1]/dt[1]/a[1]/img[1]'
        # self.album_name = By.XPATH, '/html[1]/body[1]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/select[1]/option[2]'
    def inkey(self,album_name):
        # self.driver.find_element(*self.choose_elem).click()
        # self.driver.find_element(*self.album_name).click()
        select = self.driver.find_element(*self.choose_elem)
        Select(select).select_by_visible_text(album_name)
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

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

class SearchGroupPage:
    def __init__(self,driver):
        self.driver = driver
        self.text_elem = By.XPATH, '/html[1]/body[1]/div[3]/div[1]/dl[1]/dt[1]/a[1]'
    def get_text(self):
        return self.driver.find_element(*self.text_elem).text

# /html/body/div/div[3]/div[2]/dl/dt[4]/a
# self.driver.find_element(By.ID, 'login_email').send_keys('1466306362@qq.com')
# self.driver.find_element(By.ID, 'login_pws').send_keys('020809')
# self.driver.find_element(By.ID, 'loginsubm').click()
# self.driver.find_element(By.LINK_TEXT, '退出').click()

# class LoginPage:
#     def __init__(self,driver):
#         self.user_elem = By.CSS_SELECTOR,   '#account'
#         self.pass_elem = By.CSS_SELECTOR,   '[type = "password"]'
#         self.logbutton_elem = By.CSS_SELECTOR,   '#submit'
#         self.uesr_name_elem = By.CLASS_NAME,    'user-name'
#         self.logout_elem = By.LINK_TEXT,    '退出'
#         self.driver = driver
#
#     def imput_username(self,username):
#         self.driver.find_element(*self.user_elem).clear()
#         self.driver.find_element(*self.user_elem).send_keys(username)
#
#     def imput_password(self,password):
#         self.driver.find_element(*self.pass_elem).clear()
#         self.driver.find_element(*self.pass_elem).send_keys(password)
#
#     def click_login(self):
#         self.driver.find_element(*self.logbutton_elem).click()
#
#     def logout(self):
#         self.driver.find_element(*self.uesr_name_elem).click()
#         self.driver.find_element(*self.logout_elem).click()