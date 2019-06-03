# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:34
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_1_login.py
# @Software : PyCharm
from TestDatas import login_datas as ld
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageObjects.home_page import HomePage
from PageLocators.homePage_locator import HomePageLocator
import time
import pytest
@pytest.mark.usefixtures("set_class")#整个套件setupClass
@pytest.mark.usefixtures("case_login")#
class TestLogin:
    #异常场景：密码错误、用户名错误
    @pytest.mark.parametrize("data",ld.wrong_data)#测试数据分离，有几组数据，运行几次
    def test_login_1_error(self,data,set_class):
        #操作步骤：登录——处理alert
        set_class[1].login(data["user"],data["pwd"])
        msg = set_class[1].switch_alert()
        assert data["msg"]==msg
    # 正常场景：登录成功
    @pytest.mark.smoke#用例标记
    def test_login_2_sucess(self,set_class):
        #操作步骤:登录——处理alert
        set_class[1].login(ld.sucess_data["user"], ld.sucess_data["pwd"])
        set_class[1].switch_alert()
        assert HomePage(set_class[0]).is_user_link_exists() == True



