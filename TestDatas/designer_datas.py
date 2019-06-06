# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:38
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : designer_datas.py
# @Software : PyCharm
#新建作业，作业名称
jobname = "auto_test_2222"
none_job_name=''
job_new_name = "auto_test_2223"

none_tosat = "业务名称不能为空!"
sucess_toast = "业务添加成功!"
same_toast = "作业名称重复，请重新修改"

#远程服务器信息
remote_ip='172.16.12.28'
remote_port=22
remote_username='root'
remote_pwd='yoyosys'
remote_dir="/user/liqitest/auto_text_01"

#清除远程服务器，文件的内容命令
delete_cmd="> /user/liqitest/auto_text_01"

#新增数据源add_source(source_name,ip,port,user_name,pass_word,db_name)
sucess_source ={
    "source_name":"自动化测试数据源一",
    "ip":"172.16.12.28",
    "port":"3306",
    "user_name":"root",
    "pass_word":"root",
    "db_name":"echod"
}


#目标数据target_data
target_data ={
    "source_name":"自动化测试目标源一",
    "ip":"172.16.12.28",
    "port":"3306",
    "user_name":"root",
    "pass_word":"root",
    "db_name":"echod"
}