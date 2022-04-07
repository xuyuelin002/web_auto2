#!/usr/bin/env python
# coding:utf-8
'''
@author: xuyuelin
@file: test_create_log.py
@time: 2022-03-31 15:40
@desc:
'''

import logging
from iWebSNS_unittest_frameword.config.config import log_path

# 定义日志装置
logger = logging.getLogger()
# 设置日志的记录级别INFO,ERROR,DEBUG,WARNING
logger.setLevel(logging.INFO)
# 设置记录的格式
format = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")

logfile = log_path
f = logging.FileHandler(logfile, mode='a',encoding='utf-8')
f.setLevel(logging.INFO)
f.setFormatter(format)
logger.addHandler(f)

