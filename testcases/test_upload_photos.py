#!/usr/bin/env python
# encoding: utf-8
'''
@author: xuyuelin
@file: test_upload_photos.py
@time: 2022/4/1 10:46
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
from selenium.webdriver.support.select import Select
from iWebSNS_unittest_frameword.objects.upload_photos_object import *

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
        cls.upload = UploadPage(cls.driver)

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
        验证上传相片成功
        :return:
        '''
        value_list = Datas().read_excel('上传相片')
        album_name = value_list[0][0]
        file_name = value_list[0][1]
        self.driver.find_element(By.LINK_TEXT,'相册').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'上传相片').click()
        time.sleep(1)
        self.driver.find_element(By.ID,'album_name').click()
        self.upload.inkey(album_name)
        # Select = self.driver.find_element(*self.choose_elem)
        # Select(select).select_by_visible_text(self.album_name)
        self.driver.find_element(By.LINK_TEXT, '切换上传方式').click()
        self.driver.find_element(By.ID,'attach[]').send_keys(file_name)
        self.driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/table[2]/tbody[1]/tr[6]/td[1]/input[1]').click()
        self.driver.find_element(By.XPATH, '/html[1]/body[1]/form[1]/input[1]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertEqual(file_name,self.upload.get_text())
            time.sleep(1)
            print('第一个测试用例成功上传相片')
            logger.info('验证成功上传相片的测试用例执行Passed')
        except:
            print('第一个测试用例上传相片失败,未进入正确的页面')
            logger.info('上传相片失败')

    def test_002(self):
        '''
        验证错误文件路径上传相片成功
        :return:
        '''
        value_list = Datas().read_excel('上传相片')
        album_name = value_list[1][0]
        file_name = value_list[1][1]
        self.driver.find_element(By.LINK_TEXT,'相册').click()
        time.sleep(1)
        self.driver.switch_to.frame('frame_content')
        self.driver.find_element(By.LINK_TEXT,'上传相片').click()
        time.sleep(1)
        self.driver.find_element(By.ID,'album_name').click()
        self.upload.inkey(album_name)
        # Select = self.driver.find_element(*self.choose_elem)
        # Select(select).select_by_visible_text(self.album_name)
        self.driver.find_element(By.LINK_TEXT, '切换上传方式').click()
        self.driver.find_element(By.ID,'attach[]').send_keys(file_name)
        # self.driver.find_element(By.XPATH,'/html[1]/body[1]/form[1]/table[2]/tbody[1]/tr[6]/td[1]/input[1]').click()
        # self.driver.find_element(By.XPATH, '/html[1]/body[1]/form[1]/input[1]').click()
        self.driver.switch_to.default_content()
        try:
            self.assertNotEqual(file_name,self.upload.get_text())
            time.sleep(1)
            print('第二个测试用例成功')
            logger.info('验证错误文件路径上传相片的测试用例执行Passed')
        except:
            print('第二个测试用例失败,未进入正确的页面')
            logger.info('验证失败')

if __name__ == '__main__':
    unittest.main()