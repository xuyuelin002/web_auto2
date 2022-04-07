# encoding: utf-8
'''
@author: xuyuelin
@file: test_create_log.py
@time: 2022-03-31 15:40
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
from iWebSNS_unittest_frameword.objects.create_log_object import *

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
        cls.createlog = CreateLogPage(cls.driver)

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
        验证创建日志成功
        :return:
        '''
        value_list = Datas().read_excel('创建日志')
        blog_title = value_list[0][0]
        KINDEDITORBODY = value_list[0][1]
        self.driver.find_element(By.LINK_TEXT,'日志').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'新建日志').click()
        time.sleep(1)
        self.driver.find_element(By.NAME,'blog_title').send_keys(blog_title)
        self.driver.switch_to.frame('KINDEDITORIFRAME')
        self.driver.find_element(By.ID,'KINDEDITORBODY').send_keys(KINDEDITORBODY)
        time.sleep(1)

        self.driver.switch_to.default_content()
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.XPATH,'//tr[8]//td[1]//input[1]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertEqual(blog_title,self.createlog.get_text())
            time.sleep(1)
            print('第一个测试用例成功创建日志')
            logger.info('验证成功创建日志的测试用例执行Passed')
        except:
            print('第一个测试用例创建日志失败,未进入正确的页面')
            logger.info('创建日志失败')
        # js = 'var q=document.documentElement.scrollTop=0'
        # self.driver.execute_script(js)

    def test_002(self):
        '''
        验证空日志名创建日志成功
        :return:
        '''
        value_list = Datas().read_excel('创建日志')
        blog_title = value_list[1][0]
        KINDEDITORBODY = value_list[1][1]
        self.driver.find_element(By.LINK_TEXT,'日志').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'新建日志').click()
        time.sleep(1)
        self.driver.find_element(By.NAME,'blog_title').send_keys(blog_title)
        self.driver.switch_to.frame('KINDEDITORIFRAME')
        self.driver.find_element(By.ID,'KINDEDITORBODY').send_keys(KINDEDITORBODY)
        time.sleep(1)

        self.driver.switch_to.default_content()
        js = 'var q=document.documentElement.scrollTop=1000'
        self.driver.execute_script(js)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.XPATH,'//tr[8]//td[1]//input[1]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertNotEqual(blog_title,self.createlog.get_text())
            time.sleep(1)
            print('第二个测试用例成功')
            logger.info('验证空日志名创建日志的测试用例执行Passed')
        except:
            print('第二个测试用例失败,未进入正确的页面')
            logger.info('验证失败')

if __name__ == '__main__':
    unittest.main()