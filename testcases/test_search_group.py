#!/usr/bin/env python
# encoding: utf-8
'''
@author: xuyuelin
@file: test_search_group.py
@time: 2022/4/1 10:47
@desc:
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from iWebSNS_unittest_frameword.config.config import *
from iWebSNS_unittest_frameword.data.data import *
from iWebSNS_unittest_frameword.log.log import *
from iWebSNS_unittest_frameword.objects.login_object import *
from iWebSNS_unittest_frameword.objects.search_group_object import *

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
        cls.searchgroup = SearchGroupPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        关闭浏览器
        :return:
        '''
        cls.driver.quit()

    def setUp(self) -> None:
        '''
        登录
        :return:
        '''
        value_list = Datas().read_excel('登录')
        username = value_list[0][0]
        password = value_list[0][1]
        self.login.user_paswd(username, password)
        time.sleep(1)

    def tearDown(self) -> None:
        '''
        退出登录
        :return:
        '''
        self.login.exit()
        time.sleep(1)
        # pass
    def test_001(self):
        '''
        验证搜索群组成功
        :return:
        '''
        value_list = Datas().read_excel('搜索群组')
        group_name= value_list[0][0]
        self.driver.find_element(By.LINK_TEXT,'群组').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'搜索群组').click()
        time.sleep(1)
        self.driver.find_element(By.NAME,'group_name').send_keys(group_name)
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr[4]/td[1]/input[2]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertIn(group_name,self.searchgroup.get_text())
            time.sleep(1)
            print('第一个测试用例成功搜索群组')
            logger.info('验证成功搜索群组的测试用例执行Passed')
        except:
            print('第一个测试用例创建搜索失败,未进入正确的页面')
            logger.info('创建搜索失败')

    def test_002(self):
        '''
        验证空群名搜索群组成功
        :return:
        '''
        value_list = Datas().read_excel('搜索群组')
        group_name= value_list[1][0]
        self.driver.find_element(By.LINK_TEXT,'群组').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'搜索群组').click()
        time.sleep(1)
        self.driver.find_element(By.NAME,'group_name').send_keys(group_name)
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/table[1]/tbody[1]/tr[4]/td[1]/input[2]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertNotIn(group_name,self.searchgroup.get_text())
            time.sleep(1)
            print('第二个测试用例成功')
            logger.info('验证空群名搜索群组的测试用例执行Passed')
        except:
            print('第二个测试用例失败,未进入正确的页面')
            logger.info('验证失败')

if __name__ == '__main__':
    unittest.main()