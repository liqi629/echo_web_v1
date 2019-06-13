# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 17:13
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_2_home.py
# @Software : PyCharm
from PageObjects.home_page import HomePage as hp
from TestDatas.home_datas import operation_system as os
from TestDatas.home_datas import script
from TestDatas import Common_Datas as CD
import pytest
import time
@pytest.mark.usefixtures("class_home")#
@pytest.mark.usefixtures("case_home")#
class TestHome:
    #页面切换——数据源管理
    def test_1_home_to_data_source(self,class_home):
        # 操作步骤：点击数据源管理——判断是否切换到数据源管理页——退出iframe（退出操作进行优化？？？）
        hp(class_home[0]).into_data_source()
        msg = hp(class_home[0]).is_data_source()
        assert msg==True
    #页面切换——业务系统/应用管理
    def test_2_home_to_operation_system(self,class_home):
        hp(class_home[0]).into_operation_system()
        msg = hp(class_home[0]).is_operation_system()
        assert msg == True
    #添加一个业务系统
    def test_3_add_operation_system(self,class_home):
        hp(class_home[0]).add_operation_system(os["zh_name"],os["code"],os["short_zn_name"],os["en_name"],os["short_en_name"],os["sys_remark"],os["sys_version"],os["dept"],os["contacter"],os["mobile"],os["email"])
        msg = hp(class_home[0]).is_add_operation_system()
        assert msg == True
    #删除一个业务系统
    def test_3_delete_operation_system(self, class_home):
        hp(class_home[0]).delete_operation_system()
        msg = hp(class_home[0]).is_add_operation_system()
        assert msg == False


    # 页面跳转——脚本管理
    def test_4_home_to_script(self,class_home):
        #操作步骤：
        hp(class_home[0]).into_script_manager()
        assert hp(class_home[0]).is_script_manager()==True
    #添加脚本
    def test_5_add_script(self,class_home):
        hp(class_home[0]).add_script(script["name"],script["AP"],script["content"],script["ip"],script["scriptType"],script["dbType"])
        assert hp(class_home[0]).is_addScript()==True
    #删除脚本
    def test_6_del_script(self,class_home):
        hp(class_home[0]).delScript()
        assert hp(class_home[0]).is_delScript()==True
    #页面跳转——设计器，此用例，打开了新的浏览器窗口。暂时放在最后运行
    # @pytest.mark.flaky(reruns=5, reruns_delay=1)
    @pytest.mark.skip
    def test_5_home_jump_designer(self,class_home):
        #操作步骤:跳转页面，判断
        hp(class_home[0]).into_designer()
        msg = hp(class_home[0]).is_jump_designer()
        assert msg==True






