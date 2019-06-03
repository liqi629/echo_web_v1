# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:19
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_3_designer.py
# @Software : PyCharm
from PageObjects.designer_page import DesignerPage
from TestDatas import designer_datas
from TestDatas.designer_datas import sucess_source as ss
from TestDatas.designer_datas import target_data as td
from Common.do_mysql import DoMysql
import pytest
@pytest.mark.usefixtures("set_class_home")#整个套件setupClass
@pytest.mark.usefixtures("case_designer")#整个套件setupClass
class TestDesigner:
    #空名称新增
    def test_1_none_name(self,set_class_home):
        DesignerPage(set_class_home[0]).none_job_name(designer_datas.none_job_name)
        msg = DesignerPage(set_class_home[0]).toast_text()
        assert designer_datas.none_tosat ==msg
    #新建作业
    def test_2_add_job(self,set_class_home):
        #操作步骤，新建作业，获取toast，断言
        DesignerPage(set_class_home[0]).add_job(designer_datas.jobname)
        msg = DesignerPage(set_class_home[0]).toast_text()
        assert   msg == designer_datas.sucess_toast
    #接上一个用例，重新新建用例重复用例，
    def test_3_same_name(self,set_class_home):
        # 操作步骤，新建重复名称作业，获取toast，断言
        DesignerPage(set_class_home[0]).add_job(designer_datas.jobname)
        msg = DesignerPage(set_class_home[0]).toast_text()
        assert msg == designer_datas.same_toast
    #添加数据源-mysql。关联：需要有作业
    def test_4_add_data_source(self,set_class_home):
        #操作步骤：选择新建的作业，点击数据源，点击添加，填写信息，测试连接，下一步。。。完成
        DesignerPage(set_class_home[0]).select_job()
        DesignerPage(set_class_home[0]).add_source(ss["source_name"],ss["ip"],ss["port"],ss["user_name"],ss["pass_word"],ss["db_name"])
        assert DesignerPage(set_class_home[0]).is_save_map()==True
    #添加目标-mysql。关联：需要有作业
    def test_5_add_target_source(self,set_class_home):
        #操作步骤：选择新建的作业，点击目标，进行后续添加
        DesignerPage(set_class_home[0]).select_job()
        DesignerPage(set_class_home[0]).add_target_source(td["source_name"],td["ip"],td["port"],td["user_name"],td["pass_word"],td["db_name"])
        assert DesignerPage(set_class_home[0]).is_save_map()==True

    #编辑作业名称。关联：需要有作业
    def test_6_edit_job_name(self,set_class_home):
        #操作步骤：选择作业，编辑名称
        DesignerPage(set_class_home[0]).select_job()
        DesignerPage(set_class_home[0]).edit_job(designer_datas.job_new_name)
        assert DesignerPage(set_class_home[0]).is_new_name()==True
    #删除新建的作业。关联：需要有作业
    def test_7_delete_job(self,set_class_home):
        #操作步骤：删除作业，判断是否还存在
        DesignerPage(set_class_home[0]).delete_job()
        msg = DesignerPage(set_class_home[0]).is_delete_job()
        assert   msg ==True
    #本地运行作业，数据库查询结果
    def test_8_run_job_local(self,set_class_home):
        #操作步骤:发布，运行，查询表1、2，对比表2与表1，清空表2内容
        DoMysql().deletc_data()
        DesignerPage(set_class_home[0]).run_job('local')
        res = DoMysql().select_table_2()
        assert DoMysql().select_table_1()==res
    #分布式运行
    def test_9_run_job_distributed(self,set_class_home):
        #操作步骤:发布，运行，查询表1、2，对比表2与表1，清空表2内容
        DoMysql().deletc_data()
        DesignerPage(set_class_home[0]).run_job('no_local')
        res = DoMysql().select_table_2()
        assert DoMysql().select_table_1()==res

