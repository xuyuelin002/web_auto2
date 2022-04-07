#!/usr/bin/env python
# coding:utf-8
'''
@author: xuyuelin
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''

import unittest
from BeautifulReport import BeautifulReport
from iWebSNS_unittest_frameword.config.config import cases_path,report_path

cases = unittest.defaultTestLoader.discover(start_dir=cases_path,pattern='test*.py')
result = BeautifulReport(cases)
result.report(description='iWebSNS测试报告徐悦霖', filename='第一轮测试结果徐悦霖',report_dir=report_path)
