#!/usr/bin/env python
# coding:utf-8
'''
@author: xuyuelin
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''

import os
path = os.path.dirname(os.path.dirname(__file__))
driver_path = path+r'\driver\msedgedriver.exe'
url = 'http://iwebsns.pansaifei.com/'
cases_path = path+r'\testcases'
report_path = path+r'\result'
log_path = path+r'\log\log.txt'
data_file = path+r'\data\data.xlsx'
sheetname = ('登录','创建日志','添加分类','编辑分类','创建相册','上传相片','创建群组','搜索群组') #login模块表
system_version ='v1.2'