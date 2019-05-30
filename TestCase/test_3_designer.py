# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:19
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_3_designer.py
# @Software : PyCharm
from PageObjects.designer_page import DesignerPage
from TestDatas import designer_datas
from TestDatas.designer_datas import sucess_source as ss
from Common.BasePage import BasePage
from PageLocators.designerPage_locator import DesignerPageLocator
import pytest
@pytest.mark.usefixtures("set_class_home")#整个套件setupClass
@pytest.mark.usefixtures("case_designer")#整个套件setupClass
class TestDesigner:
    #空名称新增
    def test_none_name(self,set_class_home):
        pass
    #新建作业
    def test_1_add_job(self,set_class_home):
        #操作步骤，新建作业，获取toast，断言
        DesignerPage(set_class_home[0]).add_job(designer_datas.jobname)
        msg = DesignerPage(set_class_home[0]).toast_text()
        assert   msg == designer_datas.sucess_toast
    #接上一个用例，重新新建用例
    def test_2_same_name(self,set_class_home):
        DesignerPage(set_class_home[0]).add_job(designer_datas.jobname)
        msg = DesignerPage(set_class_home[0]).toast_text()
        assert msg == designer_datas.same_toast


    #添加数据源
    def test_3_add_data_source(self,set_class_home):
        #操作步骤：选择新建的作业，点击数据源，点击添加，填写信息，测试连接，下一步。。。完成
        DesignerPage(set_class_home[0]).select_job()
        DesignerPage(set_class_home[0]).add_source(ss["source_name"],ss["ip"],ss["port"],ss["user_name"],ss["pass_word"],ss["db_name"])
        assert DesignerPage(set_class_home[0]).is_source() == True

    #编辑作业名称
    @pytest.mark.skip
    def edit_job_name(self,set_class_home):
        DesignerPage(set_class_home[0]).select_job()
        DesignerPage(set_class_home[0])
        pass
    #删除新建的作业
    # @pytest.mark.skip()
    def test_4_delete_job(self,set_class_home):
        DesignerPage(set_class_home[0]).delete_job()
        msg = DesignerPage(set_class_home[0]).is_delete_job()
        assert   True==msg
