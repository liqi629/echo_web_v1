# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:31
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : login_datas.py
# @Software : PyCharm
#正常场景：登录成功
# sucess_data = {"user":"auto_test","pwd":"auto_test"}
sucess_data = {"user":"auto_test_2","pwd":"123456"}

#异常场景：密码错误、用户名错误
wrong_data = [
    {"user":"admin","pwd":"12a3","msg":"用户名或密码错误!"},
    {"user":"abac","pwd":"123a4","msg":"用户名或密码错误!"}
]