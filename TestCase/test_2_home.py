# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 17:13
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_2_home.py
# @Software : PyCharm
from PageObjects.home_page import HomePage as hp
from TestDatas.home_datas import operation_system as os
import pytest
@pytest.mark.usefixtures("set_class_home")#整个套件setupClass
@pytest.mark.usefixtures("case_home")#整个套件setupClass
class TestHome:
    #页面切换——数据源管理
    def test_1_home_to_data_source(self,set_class_home):
        # 操作步骤：点击数据源管理——判断是否切换到数据源管理页——退出iframe（退出操作进行优化？？？）
        hp(set_class_home[0]).into_data_source()
        msg = hp(set_class_home[0]).is_data_source()
        assert msg==True
    #页面切换——业务系统/应用管理
    def test_2_home_to_operation_system(self,set_class_home):
        hp(set_class_home[0]).into_operation_system()
        msg = hp(set_class_home[0]).is_operation_system()
        assert msg == True
    #添加一个业务系统
    @pytest.mark.demo11
    def test_3_add_operation_system(self,set_class_home):
        hp(set_class_home[0]).add_operation_system(os["zh_name"],os["code"],os["short_zn_name"],os["en_name"],os["short_en_name"],os["sys_remark"],os["sys_version"],os["dept"],os["contacter"],os["mobile"],os["email"])
        msg = hp(set_class_home[0]).is_add_operation_system()
        assert msg == True
    #删除一个业务系统
    @pytest.mark.demo11
    def test_3_delete_operation_system(self, set_class_home):
        hp(set_class_home[0]).delete_operation_system()
        msg = hp(set_class_home[0]).is_add_operation_system()
        assert msg == False
    #页面跳转——设计器
    # @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_4_home_jump_designer(self,set_class_home):
        #操作步骤:跳转页面，判断
        hp(set_class_home[0]).into_designer()
        msg = hp(set_class_home[0]).is_jump_designer()
        assert msg==True





