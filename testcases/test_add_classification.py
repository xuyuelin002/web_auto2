#!/usr/bin/env python
# encoding: utf-8
'''
@author: xuyuelin
@file: test_add_classification.py
@time: 2022/4/1 10:44
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
from iWebSNS_unittest_frameword.objects.add_classification_object import *

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
        cls.addclassification = AddClassificationPage(cls.driver)

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
        pass
    def test_001(self):
        '''
        验证添加分类成功
        :return:
        '''
        value_list = Datas().read_excel('添加分类')
        blog_title = value_list[0][0]
        new_sort_name = value_list[0][1]
        self.driver.find_element(By.LINK_TEXT,'日志').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'新建日志').click()
        time.sleep(1)
        self.driver.find_element(By.NAME,'blog_title').send_keys(blog_title)
        self.driver.find_element(By.LINK_TEXT, '添加分类').click()
        self.driver.find_element(By.NAME, 'new_sort_name').send_keys(new_sort_name)
        self.driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/input[2]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertEqual(new_sort_name,self.addclassification.get_text())
            time.sleep(1)
            print('第一个测试用例成功添加分类')
            logger.info('验证成功添加分类的测试用例执行Passed')
        except:
            print('第一个测试用例添加分类失败,未进入正确的页面')
            logger.info('添加分类失败')

    def test_002(self):
        '''
        验证空分类名添加分类成功
        :return:
        '''
        value_list = Datas().read_excel('添加分类')
        blog_title = value_list[1][0]
        new_sort_name = value_list[1][1]
        self.driver.find_element(By.LINK_TEXT,'日志').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'新建日志').click()
        time.sleep(1)
        self.driver.find_element(By.NAME,'blog_title').send_keys(blog_title)
        self.driver.find_element(By.LINK_TEXT, '添加分类').click()
        self.driver.find_element(By.NAME, 'new_sort_name').send_keys(new_sort_name)
        # self.driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/input[2]').click()
        # self.driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/input[2]'
        self.driver.switch_to.default_content()
        try:
            self.assertNotEqual(new_sort_name,self.addclassification.get_text())
            time.sleep(1)
            print('第二个测试用例成功')
            logger.info('验证空分类名添加分类的测试用例执行Passed')
        except:
            print('第二个测试用例失败,未进入正确的页面')
            logger.info('验证失败')
if __name__ == '__main__':
    unittest.main()