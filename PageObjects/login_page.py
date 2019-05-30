# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:20
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : login_page.py
# @Software : PyCharm
from Common.BasePage import BasePage
from PageLocators.loginPage_locator import LoginPageLocator as loc

#继承BasePage
class LoginPage(BasePage):

    #登录操作
    def login(self,username,password):
        # 等待用户名输入框元素可见
        self.wait_eleVisible(loc.user_input)
        #输入用户名
        self.input_text(loc.user_input,username)
        #输入密码
        self.input_text(loc.passwd_input,password)
        #点击登录
        self.click_element(loc.login_button)