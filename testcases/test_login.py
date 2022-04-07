#!/usr/bin/env python
# coding:utf-8
'''
@author: xuyuelin
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from iWebSNS_unittest_frameword.config.config import *
from iWebSNS_unittest_frameword.objects.login_object import *
from iWebSNS_unittest_frameword.data.data import *
from iWebSNS_unittest_frameword.log.log import *

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''
        打开浏览器
        :return:
        '''
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Edge(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.login = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        关闭浏览器
        :return:
        '''
        cls.driver.quit()

    def test_001(self):
        '''
        验证登陆成功
        :return:字符串 失败或成功
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[0][0]
        password = value_list[0][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertIn('我的主页',self.login.get_text())
            time.sleep(1)
            print('第一个测试用例成功登录')
            logger.info('验证成功登录的测试用例执行Passed')
        except:
            print('第一个测试用例登录失败,未进入正确的页面')
            logger.info('登录失败,未进入正确的页面')

        self.login.exit()
        time.sleep(1)

        try:
            self.assertIn('聚易社区',self.driver.title)
            print('第一个测试用例成功退出')
            logger.info('验证成功退出的测试用例执行Passed')
        except:
            print('第一个测试用例退出失败')
            logger.info('退出失败,未进入正确的页面')

    def test_002(self):
        '''
        验证错误密码登录成功
        :return:字符串 失败或成功
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[1][0]
        password = value_list[1][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertNotIn('我的主页',self.login.get_text())
            time.sleep(1)
            print('第二个测试用例成功')
            logger.info('验证错误密码登录的测试用例执行Passed')
        except:
            print('第二个测试用例失败,未进入正确的页面')
            logger.info('失败,未进入正确的页面')
            print('第二个测试用例退出失败')
            logger.info('退出失败,未进入正确的页面')

    def test_003(self):
        '''
        验证错误用户名登录成功
        :return:字符串 失败或成功
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[2][0]
        password = value_list[2][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertNotIn('我的主页',self.login.get_text())
            time.sleep(1)
            print('第三个测试用例成功')
            logger.info('验证错误用户名登录的测试用例执行Passed')
        except:
            print('第三个测试用例失败,未进入正确的页面')
            logger.info('失败,未进入正确的页面')
            print('第三个测试用例退出失败')
            logger.info('退出失败,未进入正确的页面')

    def test_004(self):
        '''
        验证空密码登录成功
        :return:字符串 失败或成功
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[3][0]
        password = value_list[3][1]
        self.login.user_paswd(username, password)
        time.sleep(1)
        try:
            self.assertNotIn('我的主页',self.login.get_text())
            time.sleep(1)
            print('第四个测试用例成功')
            logger.info('验证空密码登录的测试用例执行Passed')
        except:
            print('第四个测试用例失败,未进入正确的页面')
            logger.info('失败,未进入正确的页面')
            print('第四个测试用例退出失败')
            logger.info('退出失败,未进入正确的页面')

if __name__ == '__main__':
    unittest.main()

# import unittest
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from time import sleep
# from objects.login_object import LoginPage
# from config.config import data_file,url,sheetname,driver_path
# from data.data import Datas
# from log.log import logger
#
# class TestLogin(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print("打开浏览器")
#         e = Service(executable_path=driver_path)
#         cls.driver = webdriver.Edge(service=e)
#         cls.driver.maximize_window()
#         cls.driver.get(url)
#         cls.loginpage = LoginPage(cls.driver)
#
#     @classmethod
#     def tearDownClass(cls):
#         print("关闭浏览器")
#         cls.driver.quit()
#
#     def test_1(self):
#         '''
#         验证登录成功的测试用例
#         '''
#         value_list = Datas().read_excel(sheetname[0])
#         username = value_list[0][0]
#         password = value_list[0][1]
#         self.loginpage.imput_username(username)
#         self.loginpage.imput_password(password)
#         self.loginpage.click_login()
#         sleep(1)
#         try:
#             self.assertIn(self.driver.title,'我的地盘 - 禅道')
#             sleep(1)
#             self.loginpage.logout()
#             #print("第一个测试用例成功登录")
#             logger.info("验证登录成功的测试用例执行Passed")
#         except:
#             #print("第一个测试用例登录失败,未进入正确的页面")
#             logger.info("登录失败，未进入正确的页面")
#
#     # @unittest.skipIf()  # 强制跳过
#     def test_2(self):
#         '''
#         验证错误密码登录失败的测试用例
#         '''
#         value_list = Datas().read_excel(sheetname[0])
#         username = value_list[1][0]
#         password = value_list[1][1]
#         self.loginpage.imput_username(username)
#         self.loginpage.imput_password(password)
#         self.loginpage.click_login()
#         sleep(1)
#         try:
#             alert_dialog = self.driver.switch_to.alert
#             content = alert_dialog.text
#             alert_dialog.accept()
#             # 设置断言
#             self.assertIn(content, "登录失败")
#             #print("第二个测试用例验证成功")
#             logger.info("验证错误密码登录失败的测试用例执行Passed")
#         except:
#             #print("第二个测试用例验证失败")
#             logger.info("验证错误密码登录失败的测试用例执行Failed")
#
#     def test_3(self):
#         '''
#         验证不存在的用户登录失败的测试用例
#         '''
#         value_list = Datas().read_excel(sheetname[0])
#         username = value_list[2][0]
#         password = value_list[2][1]
#         self.loginpage.imput_username(username)
#         self.loginpage.imput_password(password)
#         self.loginpage.click_login()
#         sleep(1)
#         try:
#             alert_dialog = self.driver.switch_to.alert
#             content = alert_dialog.text
#             alert_dialog.accept()
#             self.assertIn(content, "登录失败")
#             #print("第三个测试用例验证成功")
#             logger.info("验证不存在的用户登录失败的测试用例执行Passed")
#         except:
#             #print("第三个测试用例验证失败")
#             logger.info("验证不存在的用户登录失败的测试用例执行Failed")
#
# if __name__ == '__main__':
#     unittest.main()
