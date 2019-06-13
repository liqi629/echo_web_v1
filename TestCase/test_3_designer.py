# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:19
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : test_3_designer.py
# @Software : PyCharm
from PageObjects.designer_page import DesignerPage
from TestDatas import designer_datas as dd
from TestDatas.designer_datas import sucess_source as ss
from TestDatas.designer_datas import target_data as td
from Common.do_mysql import DoMysql
from Common.remote import Remote
from Common import dir_config
from Common.do_file import DoFile
import time
import pytest
@pytest.mark.usefixtures("class_home")#整个类的前置
@pytest.mark.usefixtures("case_designer")#测试用例的前置
class TestDesigner:
    #空名称新增
    def test_1_none_name(self,class_home):
        DesignerPage(class_home[0]).none_job_name(dd.none_job_name)
        msg = DesignerPage(class_home[0]).toast_text()
        assert msg==dd.none_tosat
    #新建作业
    @pytest.mark.flaky(reruns=1, reruns_delay=10)
    def test_2_add_job(self,class_home):
        #操作步骤，新建作业，获取toast，断言
        DesignerPage(class_home[0]).add_job(dd.jobname)
        msg = DesignerPage(class_home[0]).toast_text()
        assert   msg == dd.sucess_toast
    #接上一个用例，重新新建用例重复用例，
    def test_3_same_name(self,class_home):
        # 操作步骤，新建重复名称作业，获取toast，断言
        DesignerPage(class_home[0]).add_job(dd.jobname)
        msg = DesignerPage(class_home[0]).toast_text()
        assert msg == dd.toast_job_same
    #添加数据源-mysql。关联：需要有作业
    def test_4_add_data_source(self,class_home):
        #操作步骤：选择新建的作业，点击数据源，点击添加，填写信息，测试连接，下一步。。。完成
        DesignerPage(class_home[0]).add_source(ss["source_name"],ss["ip"],ss["port"],ss["user_name"],ss["pass_word"],ss["db_name"])
        assert DesignerPage(class_home[0]).is_save_map()==True
    #添加目标-mysql。关联：需要有作业
    def test_5_add_target_source(self,class_home):
        #操作步骤：选择新建的作业，点击目标，进行后续添加
        DesignerPage(class_home[0]).add_target_source(td["source_name"],td["ip"],td["port"],td["user_name"],td["pass_word"],td["db_name"])
        assert DesignerPage(class_home[0]).is_save_map()==True

    #编辑作业名称。关联：需要有作业
    @pytest.mark.flaky(reruns=1, reruns_delay=10)
    def test_6_edit_job_name(self,class_home):
        time.sleep(10)
        #操作步骤：选择作业，编辑名称
        DesignerPage(class_home[0]).edit_job(dd.job_new_name)
        assert DesignerPage(class_home[0]).is_new_name()==True
    #删除新建的作业。关联：需要有作业
    @pytest.mark.flaky(reruns=1, reruns_delay=5)#失败后5s，重新运行1次
    def test_7_delete_job(self,class_home):
        time.sleep(10)
        #操作步骤：删除作业，判断是否还存在
        DesignerPage(class_home[0]).delete_job()
        msg = DesignerPage(class_home[0]).is_delete_job()
        assert   msg ==True
    #本地运行作业:mysql-mysql，数据库查询结果
    def test_8_run_job_local(self,class_home):
        #操作步骤:发布，运行，查询表1、2，对比表2与表1，清空表2内容
        DoMysql().deletc_data()
        DesignerPage(class_home[0]).run_job('local')
        res = DoMysql().select_table_2()
        assert DoMysql().select_table_1()==res
    #分布式运行作业:mysql-mysql，
    def test_9_run_job_distributed(self,class_home):
        #操作步骤:发布，运行，查询表1、2，对比表2与表1，清空表2内容
        DoMysql().deletc_data()
        DesignerPage(class_home[0]).run_job('no_local')
        res = DoMysql().select_table_2()
        assert DoMysql().select_table_1()==res
    #本地运行作业:mysql-file，数据库查询结果
    def test_10_run_job_mysql_text_local(self,class_home):
        #操作步骤:清楚目标文本内容,运行,下载目标文件，读取目标文件name，读取数据库表name，断言
        Remote().cmd(dd.remote_ip,dd.remote_port,dd.remote_username,dd.remote_pwd,dd.delete_cmd)
        DesignerPage(class_home[0]).run_job_MySQL_text('local')
        Remote().get_file(dd.remote_ip,dd.remote_port,dd.remote_username,dd.remote_pwd,dd.remote_dir,dir_config.ftp_auto_text_01)
        mysql_name = DoMysql().select_table_1()
        assert DoFile().get_file_name()==mysql_name[0][1]

    # 分布式运行作业:mysql-file，数据库查询结果，数据库查询部分需要优化，分离sql语句
    def test_11_run_job_mysql_text_distributed(self,class_home):
        #操作步骤:清楚目标文本内容,运行,下载目标文件，读取目标文件name，读取数据库表name，断言
        Remote().cmd(dd.remote_ip,dd.remote_port,dd.remote_username,dd.remote_pwd,dd.delete_cmd)
        DesignerPage(class_home[0]).run_job_MySQL_text('no_local')
        Remote().get_file(dd.remote_ip,dd.remote_port,dd.remote_username,dd.remote_pwd,dd.remote_dir,dir_config.ftp_auto_text_01)
        mysql_name = DoMysql().select_table_1()
        assert DoFile().get_file_name()==mysql_name[0][1]

    #切换作业窗口
    def test_12_switch_job(self,class_home):
        DesignerPage(class_home[0]).switch_job()
        assert DesignerPage(class_home[0]).is_switch_job()==True

    #取消发布
    @pytest.mark.flaky(reruns=1, reruns_delay=10)
    def test_13_unpub(self,class_home):
        #操作步骤
        DesignerPage(class_home[0]).unpublish()
        msg = DesignerPage(class_home[0]).toast_text()
        assert msg == dd.toast_pub_cancel
    #发布作业
    def test_14_pub(self,class_home):
        #操作步骤
        DesignerPage(class_home[0]).publish()
        msg = DesignerPage(class_home[0]).toast_text()
        assert msg in dd.toast_pubing
    #重复发布
    @pytest.mark.flaky(reruns=1, reruns_delay=10)
    def test_15_same_pub(self,class_home):
        # 操作步骤
        DesignerPage(class_home[0]).publish()
        msg = DesignerPage(class_home[0]).toast_text()
        assert msg in dd.toast_pubing
    #运行工作流脚本
    def test_16_work_flow(self,class_home):
        #操作步骤：直接打开工作流网址，运行，断言
        class_home[0].get(dd.work_flow_url)
        DesignerPage(class_home[0]).run_work_flow()
        assert DesignerPage(class_home[0]).is_work_flow()==True
    #新建工作流
    def test_17_add_work_flow(self,class_home):
        #操作步骤，选择作业note_delete,点击展开，点击/鼠标悬浮工作流，点击添加按钮，弹窗输入工作流名称，输入内容，点击确定，断言
        DesignerPage(class_home[0]).add_work_flow(dd.work_flow_name)
        assert DesignerPage(class_home[0]).is_new_work_flow()==True
    #新建工作流名字重复
    def test_18_add_work_flow(self,class_home):
        DesignerPage(class_home[0]).add_work_flow(dd.work_flow_name)
        assert dd.same_flow_name == DesignerPage(class_home[0]).toast_text()
    #删除工作流
    def test_19_del_work_flow(self,class_home):
        DesignerPage(class_home[0]).delete_work_flow()
        assert  DesignerPage(class_home[0]).is_delete_work_flow()==True

