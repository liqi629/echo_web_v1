# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:11
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : loginPage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
class LoginPageLocator:
    #用户名输入框
    user_input = (By.XPATH, '//input[@id="name"]')
    #密码输入框
    passwd_input = (By.XPATH, '//input[@id="inputPassword"]')
    #登陆按钮
    login_button = (By.XPATH, '//a[@id="login"]')
