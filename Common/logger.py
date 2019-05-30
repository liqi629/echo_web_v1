# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:06
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : logger.py
# @Software : PyCharm
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from Common import dir_config

#设置格式
fmt = "%(asctime)s-%(levelname)s-%(filename)s-%(funcName)s-[line:%(lineno)d]%(message)s"
datefmt = "%a, %d %b %Y %H:%M:%S"
#创建实例，输出到控制台
handler_1 = logging.StreamHandler()
curTime = time.strftime("%Y-%m-%d %H%M",time.localtime())

handler_2 = RotatingFileHandler(dir_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime),backupCount=0,encoding='utf-8')
#设置rootlogger的输出内容形式，输出渠道
logging.basicConfig(format=fmt,datefmt=datefmt,level=logging.INFO,handlers=[handler_1,handler_2])

# logging.info("hhehehe")