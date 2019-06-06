# -*- coding: utf-8 -*-
# @Time     : 2019/6/5 11:07
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : do_text.py
# @Software : PyCharm
from numpy.compat import basestring

from Common.do_mysql import DoMysql
from Common import dir_config
f = open(dir_config.ftp_auto_text_01,encoding='utf-8')

lines = f.read()

txt = lines
print("txt取到的信息"+txt[2]+txt[3]+txt[4])
f.close()
t1 = DoMysql().select_table_1()
res = t1[0]
print(t1[0][1])
print(res[1])
# print(txt[2]+txt[3]+txt[4]==res[1])
# ff=open("D:\YOYO\\auto_web_echo_v1\TestDatas\demo_1.txt","w+")
# ff.truncate()
#
# ff.close()




