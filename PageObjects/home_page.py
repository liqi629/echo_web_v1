# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 14:19
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : home_page.py
# @Software : PyCharm
from PageLocators.homePage_locator import HomePageLocator as loc
from Common.BasePage import BasePage
import time
class HomePage(BasePage):
    def __init__(self,driver):
        self.driver = driver
    #判断用户名是否存在
    def is_user_link_exists(self):
        try:
            self.wait_eleVisible(loc.user_link)
            return True
        except:
            return False
    #判断是否切换到数据源管理页
    def is_data_source(self):
        try:
            self.switch_iframe(loc.iframe_data_source_manager)
            self.wait_eleVisible(loc.page_data_source_manager)
            return True
        except:
            return False
    #退出登录
    def logout(self):
        self.wait_eleVisible(loc.logout_button)
        self.click_element(loc.logout_button)
    #鼠标悬浮作业设计——点击设计器
    def into_designer(self):
        self.wait_eleVisible(loc.job_design)
        self.hover_element(loc.job_design)
        self.wait_eleVisible(loc.designer)
        self.click_element(loc.designer)
    #点击数据源管理
    def click_data_source(self):
        #等待元素【业务管理】可见，鼠标悬浮，等待【数据源管理】
        self.wait_eleVisible(loc.business_management)
        self.hover_element(loc.business_management)
        self.wait_eleVisible(loc.data_source_manager)
        self.click_element(loc.data_source_manager)