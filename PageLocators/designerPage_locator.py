# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 14:55
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : designerPage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
class DesignerPageLocator:
    #新建作业+号
    add_job=(By.XPATH,'//img[@id="addBgBac"]')
    #作业名称输入框//input[@id="bisName"]
    job_name_input = (By.XPATH, '//input[@id="bisName"]')
    #新建作业确认按钮
    job_button = (By.XPATH, '//a[@id="btnBusinessAdd"]')
    #新建作业成功/名称重复toast提示//div[@class="toast-message"]
    job_toast = (By.XPATH, '//div[@class="toast-message"]')
    #新建完成的作业，列表中的定位 //span[text()="auto_test_2"]
    job_list_new = (By.XPATH, ' //span[text()="auto_test_2222"]')
    # 编辑名称后的作业，列表中的定位 //span[text()="auto_test_3"]
    job_list_new_1 = (By.XPATH, ' //span[text()="auto_test_2223"]')
    #鼠标悬浮新建作业，删除按钮//span[text()="删除"][1]
    delete_job_button = (By.XPATH, '//span[text()="删除"][1]')
    #删除作业弹窗 的删除按钮
    dialog_delete_button = (By.XPATH, '//a[@id="btn-delete"]')

    #数据源
    data_source = (By.XPATH, '//span[text()="数据源"]')
    #添加按钮
    add_button = (By.XPATH, '//span[text()="添加"]')
    #保存按钮
    save_button = (By.XPATH,'//span[text()="保存"]')
    #数据库，树加号，展开作用//span[@id="dataTree_1_switch"]
    data_tree_1 = (By.XPATH,'//span[@id="dataTree_1_switch"]')

    #MySQL数据库，操作相关========================================================================
    #数据库-MySQL  //span[text()="MySQL"]
    MySQL = (By.XPATH,' //span[text()="MySQL"]')
    #数据库选择后的确认按钮//a[@id="btn-db-type"]
    db_button = (By.XPATH,'//a[@id="btn-db-type"]')
    #新增数据库按钮//form[@name="sameTOMysqlDriver"]//button[@id="addSource"]
    add_source = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//button[@id="addSource"]')
    #源名称输入框//form[@name="sameTOMysqlDriver"]//input[@id="sourceName"]
    source_name = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="sourceName"]')
    #ip输入框//form[@name="sameTOMysqlDriver"]//input[@id="ip"]
    ip = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="ip"]')
    #端口//form[@name="sameTOMysqlDriver"]//input[@id="port"]
    port = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="port"]')
    #用户名//form[@name="sameTOMysqlDriver"]//input[@id="userName"]
    user_name = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="userName"]')
    #密码//form[@name="sameTOMysqlDriver"]//input[@id="passWord"]
    pass_word = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="passWord"]')
    #所属系统selection://*[@id="form-fieldset"]//span[@class="select2-selection__arrow"]
    select = (By.XPATH,'//*[@id="form-fieldset"]//span[@class="select2-selection__arrow"]')
    #数据库名称//form[@name="sameTOMysqlDriver"]//input[@id="dbName"]
    db_name = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="dbName"]')
    #环境类型//form[@name="sameTOMysqlDriver"]//select[@id="environmentType"]
    environment_type = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//select[@id="environmentType"]')
    #是否跨域//form[@name="sameTOMysqlDriver"]//select[@id="crossDomain"]
    cross_domain = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//select[@id="crossDomain"]')
    #编码设置//form[@name="sameTOMysqlDriver"]//select[@id="characterEncoding"]
    character_encoding = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//select[@id="characterEncoding"]')
    #备注//form[@name="sameTOMysqlDriver"]//input[@id="remark"]
    mark = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//input[@id="remark"]')
    #测试连接按钮//form[@name="sameTOMysqlDriver"]//a[@id="test-connect"]
    test_connect = (By.XPATH,'//form[@name="sameTOMysqlDriver"]//a[@id="test-connect"]')
    #测试连接的toast://span[text()="连接成功"]
    test_msg = (By.XPATH,'//span[text()="连接成功"]')
    #上一步按钮//a[text()="上一步"]
    last_step = (By.XPATH,'//a[text()="上一步"]')
    #下一步按钮//a[text()="下一步"]
    next_step = (By.XPATH,'//a[text()="下一步"]')
    #数据库第一个表//input[@name="tableCheckList"][1]
    first_tab = (By.XPATH,'//input[@name="tableCheckList"][1]')
    #数据库第二个表
    second_tab = (By.XPATH,'//input[@name="tableCheckList"][2]')
    #选表后的下一步
    next_step = (By.XPATH,'//a[text()="下一步"]')
    #选字段信息后的下一步
    next_step = (By.XPATH,'//a[text()="下一步"]')
    #最终确定按钮
    confirm_button = (By.XPATH,'//a[text()="确定"]')
    #MySQL数据库，操作相关========================================================================

    #添加成功后的数据源
    source_title = (By.XPATH,'//span[text()="自动化测试数据源一"]')