# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 14:18
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : homePage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
class HomePageLocator:
    #用户昵称
    user_link=(By.XPATH,'//i[@class="entypo-user user"]')
    #推出按钮
    logout_button = (By.XPATH,'//a[@class="btn-logout"]')
#导航菜单=========================================================================================
    #作业设计
    job_design=(By.XPATH,'//span[text()="作业设计"]')
    #设计器
    designer=(By.XPATH,'//span[text()="设计器"]')
    #导航业务管理图标
    business_management = (By.XPATH,'//span[text()="业务管理"]')
    #子菜单数据源管理
    data_source_manager = (By.XPATH,'//span[text()="数据源管理"]')
    # 子菜单数应用管理/业务系统
    operation_system = (By.XPATH, '//span[text()="应用管理"]')
    #子菜单脚本管理
    script_manager=(By.XPATH,'//span[text()="脚本管理"]')
    #页面标题数据源管理
    page_data_source_manager = (By.XPATH,'//ol[@class="breadcrumb bc-3"]//*[text()="数据源管理"]')
    #页面标题业务体系管理/应用管理
    page_operation_system = (By.XPATH,'//strong[text()="业务系统管理"]')
    #home页iframe。业务管理、脚本管理通用
    main_frame = (By.XPATH,'//iframe[@id="mainFrame"]')
    #作业设计-脚本管理
    page_script_manager = (By.XPATH,'//ol[@class="breadcrumb bc-3"]//*[text()="脚本管理"]')
#业务系统================================================================================================
    #添加按钮
    add_button = (By.XPATH,'//a[@id="add"]')
    #中文全称输入框
    zh_name = (By.XPATH,'//div[@id="addModalTable"]//input[@id="zhName"]')
    #编码输入框
    code = (By.XPATH,'//div[@id="addModalTable"]//input[@id="code"]')
    #中文简称输入框
    short_zn_name = (By.XPATH,'// div[ @ id = "addModalTable"]//input[ @ id = "shortZhName"]')
    #英文全称
    en_name = (By.XPATH,'// div[ @ id = "addModalTable"]//input[ @ id = "enName"]')
    #英文简称
    short_en_name = (By.XPATH,'// div[ @ id = "addModalTable"]//input[ @ id = "shortEnName"]')
    #系统概述
    sys_remark = (By.XPATH,'// div[ @ id = "addModalTable"]//input[ @ id = "remark"]')
    #系统状态
    sys_status = (By.XPATH,'// div[ @ id = "addModalTable"]//select[ @ id = "status"]')
    #系统版本
    sys_version = (By.XPATH,'// div[ @ id = "addModalTable"]//input[ @ id = "version"]')
    #所属部门
    dept = (By.XPATH,'// div[ @ id = "addModalTable"] // input[ @ id = "dept"]')
    #联系人,html页面id属性值拼写有错误
    contacter = (By.XPATH,'// div[ @ id = "addModalTable"] // input[ @ id = "contactor"]')
    #联系电话
    mobile = (By.XPATH,'// div[ @ id = "addModalTable"] // input[ @ id = "mobile"]')
    #联系人邮箱
    email = (By.XPATH,'// div[ @ id = "addModalTable"] // input[ @ id = "email"]')
    #确定按钮
    ok_button = (By.XPATH,'// div[ @ id = "addModalTable"] // button[@class ="btn btn-primary btn-add"]')
    #新增成功的业务系统中文全称
    add_sys_name = (By.XPATH,'//*[text()="功能自动化测试一"]')
    #新增成功的业务系统的编辑按钮
    edit_new_sys_1_button = (By.XPATH,'//*[text()="功能自动化测试一"]//parent::tr//*[text()="编辑"]')
    # 新增成功的业务系统的删除按钮
    delete_new_sys_1_button = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="删除"]')
    # 新增成功的业务系统的查看详情按钮
    view_new_sys_1_button = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="查看详情"]')
    #删除业务系统的确定按钮
    delete_button = (By.XPATH,'// div[ @id="deleteModalTable"]//button[text()="确定"]')
    # 删除业务系统的取消按钮
    cancel_button = (By.XPATH,'// div[ @id="deleteModalTable"]//button[text()="取消"]')


#脚本管理=============================================================================================================
    #添加按钮:add_button,与业务系统的添加按钮元素定位一样

    #脚本操作类型
    select_scriptType=(By.XPATH,'//form[@id="addForm"]//select[@id="scriptType"]')
    #DBselect定位//div[@id="modalTable"]//select[@id="dbType"]
    select_dbType=(By.XPATH,'//form[@id="addForm"]//select[@id="dbType"]')

    scriptName = (By.XPATH,'//div[@id="addModalTable"]//input[@id="name"]')
    #脚本路径
    scriptPath =(By.XPATH,'//div[@id="addModalTable"]//input[@id="scriptPath"]')
    #脚本内容输入框
    scriptContent =(By.XPATH,'//div[@id="addModalTable"]//textarea[@id="scriptContent"]')
    #执行ip
    scripyIp = (By.XPATH,'//div[@id="addModalTable"]//input[@class="proval form-control"]')
    #提交
    btn_sub=(By.XPATH,'//div[@id="addModalTable"]//button[text()="提交"]')
    #新增的脚本
    scriptText=(By.XPATH,'//td[text()="auto_script_01.sh"]')
    #新增脚本的删除按钮
    btnDelScript=(By.XPATH,'//td[text()="auto_script_01.sh"]//parent::tr//*[text()="删除"]')
    #确定删除按钮//div[@id="deleteModalTable"]//button[text()="确定"]
    btnConfirm=(By.XPATH,'//div[@id="deleteModalTable"]//button[text()="确定"]')







