# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 17:25
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : login.py
# @Software : PyCharm
from selenium import webdriver
from PageLocators.loginPage_locator import LoginPageLocator as loc
from PageObjects.login_page import LoginPage
from TestDatas import Common_Datas
from TestDatas import login_datas
from Common.BasePage import BasePage
import time
def login():
    url = Common_Datas.login_url
    info = login_datas.sucess_data
    driver = webdriver.Firefox()
    driver.get(url)
    lp = LoginPage(driver)
    lp.login(info["user"],info["pwd"])
    alert = lp.switch_alert(driver)
    if alert:
        msg = alert.text
        print(msg)
        alert.accept()
    else:
        print("alert未弹出！")
    return driver


