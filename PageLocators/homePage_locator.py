# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 14:18
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : homePage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
class HomePageLocator:
    #用户昵称
    user_link=(By.XPATH,'//i[@class="entypo-user user"]')
    #推出按钮
    logout_button = (By.XPATH,'//a[@class="btn-logout"]')
    #作业设计
    job_design=(By.XPATH,'//i[@class="entypo-layout"]')
    #设计器
    designer=(By.XPATH,'//span[text()="设计器"]')
    #导航业务管理图标
    business_management = (By.XPATH,'//i[@class="entypo-database"]')
    #子菜单数据源管理
    data_source_manager = (By.XPATH,'//span[text()="数据源管理"]')
    #页面标题数据源管理
    page_data_source_manager = (By.XPATH,'//ol[@class="breadcrumb bc-3"]//*[text()="数据源管理"]')
    #数据源管理iframe
    iframe_data_source_manager = (By.XPATH,'//iframe[@id="mainFrame"]')


