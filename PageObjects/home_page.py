# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 14:19
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : home_page.py
# @Software : PyCharm
from PageLocators.homePage_locator import HomePageLocator as loc
from PageLocators.designerPage_locator import DesignerPageLocator
from Common.BasePage import BasePage
from selenium.webdriver.support.ui import Select
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
            self.switch_iframe(loc.main_frame)
            self.wait_eleVisible(loc.page_data_source_manager)
            return True
        except:
            return False
        self
    # 判断是否切换到应用管理/业务系统管理页
    def is_operation_system(self):
        try:
            self.switch_iframe(loc.main_frame)
            self.wait_eleVisible(loc.page_operation_system)
            return True
        except:
            return False
    # 判断是否打开了设计器页面
    def is_jump_designer(self):
        try:
            #根据元素 数据源是否可见来判断
            self.wait_eleVisible(DesignerPageLocator.data_source)
            return True
        except:
            return False
    # 判断是否切切换到了脚本管理页面
    def is_script_manager(self):
        try:
            self.switch_iframe(loc.main_frame)
            self.wait_eleVisible(loc.page_script_manager)
            return True
        except:
            return False
    #退出登录
    def logout(self):
        self.wait_eleVisible(loc.logout_button)
        self.click_element(loc.logout_button)
    #鼠标悬浮作业设计——点击设计器，进入新窗口
    def into_designer(self):
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        self.wait_eleVisible(loc.job_design)
        self.hover_element(loc.job_design)
        self.wait_eleVisible(loc.designer)
        self.click_element(loc.designer)
        # 切换到新窗口
        self.switch_window("new", current_handles)
        time.sleep(1)  # 加硬等待，增强稳定性
    #点击数据源管理
    def into_data_source(self):
        #等待元素【业务管理】可见，鼠标悬浮，等待【数据源管理】
        self.wait_eleVisible(loc.business_management)
        self.hover_element(loc.business_management)
        self.wait_eleVisible(loc.data_source_manager)
        self.click_element(loc.data_source_manager)
    #点击应用管理/业务系统管理
    def into_operation_system(self):
        self.wait_eleVisible(loc.business_management)
        self.hover_element(loc.business_management)
        self.wait_eleVisible(loc.operation_system)
        self.click_element(loc.operation_system)
    #点击进入脚本管理页面
    def into_script_manager(self):
        self.wait_eleVisible(loc.job_design)
        self.hover_element(loc.job_design)
        self.wait_eleVisible(loc.script_manager)
        self.click_element(loc.script_manager)
    #dbType select操作
    def select_dbType(self,text):
        s = self.select(loc.select_dbType)
        s.select_by_visible_text(text)

    # dbType select操作
    def select_scriptType(self, text):
        s = self.select(loc.select_scriptType)
        s.select_by_visible_text(text)
        # s.select_by_value(11)
        # 1、下标
        # s.deselect_by_index()
        # # 2、value属性
        # s.deselect_by_value(11)
        # # 3、文本内容
        # s.deselect_by_visible_text("其他")
        pass

    #添加脚本
    def add_script(self,name,path,content,ip,text1,text2):
        self.into_script_manager()
        # 切入iframe页面进行操作
        self.switch_iframe(loc.main_frame)
        #点击添加按钮
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        #输入脚本名字
        self.wait_eleVisible(loc.scriptName)
        self.input_text(loc.scriptName,name)
        #输入脚本绝对路径
        self.wait_eleVisible(loc.scriptPath)
        self.input_text(loc.scriptPath,path)
        #select 操作
        self.select_scriptType(text1)
        self.select_dbType(text2)
        self.wait_eleVisible(loc.scriptContent)
        self.input_text(loc.scriptContent,content)
        self.input_text(loc.scripyIp,ip)
        time.sleep(2)
        self.click_element(loc.btn_sub)
        time.sleep(2)
    #判断脚本是否添加成功
    def is_addScript(self):
        try:
            self.wait_eleVisible(loc.scriptText)
            return True
        except:
            False
    #删除新增脚本
    def delScript(self):
        self.into_script_manager()
        # 切入iframe页面进行操作
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.btnDelScript)
        self.click_element(loc.btnDelScript)
        self.wait_eleVisible(loc.btnConfirm)
        self.click_element(loc.btnConfirm)
    #判断是否删除成功
    def is_delScript(self):
        try:
            self.wait_eleVisible(loc.scriptText,timeout=3)
            return True
        except: False
    #添加业务系统
    def add_operation_system(self,zh_name,code,short_zn_name,en_name,short_en_name,sys_remark,sys_version,dept,contacter,mobile,email):
        #调用进入业务系统管理页面的函数
        self.into_operation_system()
        #切入iframe页面进行操作
        self.switch_iframe(loc.main_frame)
        #点击添加按钮：输入信息
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        self.wait_eleVisible(loc.zh_name)
        self.input_text(loc.zh_name,zh_name)
        self.wait_eleVisible(loc.code)
        self.input_text(loc.code, code)
        self.wait_eleVisible(loc.short_zn_name)
        self.input_text(loc.short_zn_name, short_zn_name)
        self.wait_eleVisible(loc.en_name)
        self.input_text(loc.en_name, en_name)
        self.wait_eleVisible(loc.short_en_name)
        self.input_text(loc.short_en_name, short_en_name)
        self.wait_eleVisible(loc.sys_remark)
        self.input_text(loc.sys_remark, sys_remark)
        self.wait_eleVisible(loc.sys_version)
        self.input_text(loc.sys_version, sys_version)
        self.wait_eleVisible(loc.dept)
        self.input_text(loc.dept, dept)
        self.wait_eleVisible(loc.contacter)
        self.input_text(loc.contacter, contacter)
        self.wait_eleVisible(loc.mobile)
        self.input_text(loc.mobile, mobile)
        self.wait_eleVisible(loc.email)
        self.input_text(loc.email, email)
        self.wait_eleVisible(loc.ok_button)
        self.click_element(loc.ok_button)
    #判断新增的业务系统是否存在
    def is_add_operation_system(self):
        try:
            self.wait_eleVisible(loc.add_sys_name,timeout=3)
            return True
        except:
            return False
    #删除一个业务系统
    def delete_operation_system(self):
        # 调用进入业务系统管理页面的函数
        self.into_operation_system()
        # 切入iframe页面进行操作
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.delete_new_sys_1_button)
        self.click_element(loc.delete_new_sys_1_button)
        time.sleep(2)
        self.wait_eleVisible(loc.delete_button)
        self.click_element(loc.delete_button)
        time.sleep(2)

