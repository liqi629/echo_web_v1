# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:09
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : designer_page.py
# @Software : PyCharm
from Common.BasePage import BasePage
from PageLocators.designerPage_locator import DesignerPageLocator as loc
import time
#继承BasePage
class DesignerPage(BasePage):
    #新建作业
    def add_job(self,jobname):
        # 等待+号元素可见
        self.wait_eleVisible(loc.add_job)
        #点击新建作业的加号
        self.click_element(loc.add_job)
        #等待作业名称输入框可见
        self.wait_eleVisible(loc.job_name_input)
        #清空输入框
        self.clear_input_text(loc.job_name_input)
        #输入作业名称
        self.input_text(loc.job_name_input,jobname)
        #点击确定按钮
        self.click_element(loc.job_button)

    #获取新建作业成功的(名称重复的的)toast，文本

    def toast_text(self):
        #加入等待toast可见，否则会报错，时间太快获取不到toast
        self.wait_eleVisible(loc.job_toast)
        return self.get_text(loc.job_toast)
    #点击选择新建的作业
    def select_job(self):
        self.wait_eleVisible(loc.job_list_new)
        self.click_element(loc.job_list_new)
    #编辑作业名称
    
    # 删除新建的作业
    def delete_job(self):
        #等待新建作业可见
        self.wait_eleVisible(loc.job_list_new)
        #鼠标悬浮
        self.hover_element(loc.job_list_new)
        #点击删除按钮
        self.wait_eleVisible(loc.delete_job_button)
        self.click_element(loc.delete_job_button)
        time.sleep(2)
        #点击dialog中的删除
        self.wait_eleVisible(loc.dialog_delete_button)
        self.click_element(loc.dialog_delete_button)
        time.sleep(2)
    #判断新建的作业是否被删除
    def is_delete_job(self):
        try:
            self.get_Element(loc.job_list_new)
            return False
        except:
            return True
    #添加数据源
    def add_source(self,source_name,ip,port,user_name,pass_word,db_name):
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        #点击数据源
        self.wait_eleVisible(loc.data_source)
        self.click_element(loc.data_source)
        #点击添加按钮
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        #展开对象树
        self.wait_eleVisible(loc.data_tree_1)
        self.click_element(loc.data_tree_1)
        #选择点击MySQL
        self.wait_eleVisible(loc.MySQL)
        self.click_element(loc.MySQL)
        #点击确定按钮

        self.wait_eleVisible(loc.db_button)
        self.click_element(loc.db_button)

        #切换到新窗口
        self.switch_window("new",current_handles)
        self.wait_eleVisible(loc.add_source)
        time.sleep(1)#加硬等待，增强稳定性
        #点击新增
        self.click_element(loc.add_source)
        #输入数据源名称
        self.input_text(loc.source_name,source_name)
        #输入ip、端口
        self.input_text(loc.ip,ip)
        self.input_text(loc.port,port)
        #输入用户名、密码
        self.input_text(loc.user_name,user_name)
        self.input_text(loc.pass_word,pass_word)
        #选择所属系统
        pass
        #输入数据库名称
        self.input_text(loc.db_name,db_name)
        #选择环境类型
        pass
        #选择是否跨域
        pass
        #编码设置
        pass
        #备注
        pass
        #点击测试连接
        self.click_element(loc.test_connect)
        # return self.get_text(loc.test_msg)
        #点击下一步
        self.click_element(loc.next_step)
        time.sleep(0.5)
        #选择数据库的第一个表
        self.wait_eleVisible(loc.first_tab)
        self.click_element(loc.first_tab)
        time.sleep(0.5)
        #点击下一步
        self.click_element(loc.next_step)
        time.sleep(0.5)
        #继续点击下一步
        self.wait_eleVisible(loc.next_step)
        self.click_element(loc.next_step)
        time.sleep(1)
        #点击确定按钮
        self.wait_eleVisible(loc.confirm_button)
        self.click_element(loc.confirm_button)
        time.sleep(1)

        # 切换回html窗口
        self.switch_window("default",current_handles)
        time.sleep(1)
    #判断新添加的数据源节点是否存在
    def is_source(self):

        try:
            self.wait_eleVisible(loc.source_title)
            return True
        except:
            False



