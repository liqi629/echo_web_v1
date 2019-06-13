# -*- coding: utf-8 -*-
# @Time     : 2019/6/12 16:08
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : operationSystemPage.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
#业务系统管理
class OperationSystemPage:
    # 添加按钮
    add_button = (By.XPATH, '//a[@id="add"]')
    # 中文全称输入框
    zh_name = (By.XPATH, '//div[@id="addModalTable"]//input[@id="zhName"]')
    # 编码输入框
    code = (By.XPATH, '//div[@id="addModalTable"]//input[@id="code"]')
    # 中文简称输入框
    short_zn_name = (By.XPATH, '// div[ @ id = "addModalTable"]//input[ @ id = "shortZhName"]')
    # 英文全称
    en_name = (By.XPATH, '// div[ @ id = "addModalTable"]//input[ @ id = "enName"]')
    # 英文简称
    short_en_name = (By.XPATH, '// div[ @ id = "addModalTable"]//input[ @ id = "shortEnName"]')
    # 系统概述
    sys_remark = (By.XPATH, '// div[ @ id = "addModalTable"]//input[ @ id = "remark"]')
    # 系统状态
    sys_status = (By.XPATH, '// div[ @ id = "addModalTable"]//select[ @ id = "status"]')
    # 系统版本
    sys_version = (By.XPATH, '// div[ @ id = "addModalTable"]//input[ @ id = "version"]')
    # 所属部门
    dept = (By.XPATH, '// div[ @ id = "addModalTable"] // input[ @ id = "dept"]')
    # 联系人,html页面id属性值拼写有错误
    contacter = (By.XPATH, '// div[ @ id = "addModalTable"] // input[ @ id = "contactor"]')
    # 联系电话
    mobile = (By.XPATH, '// div[ @ id = "addModalTable"] // input[ @ id = "mobile"]')
    # 联系人邮箱
    email = (By.XPATH, '// div[ @ id = "addModalTable"] // input[ @ id = "email"]')
    # 确定按钮
    ok_button = (By.XPATH, '// div[ @ id = "addModalTable"] // button[@class ="btn btn-primary btn-add"]')
    # 新增成功的业务系统中文全称
    add_sys_name = (By.XPATH, '//*[text()="功能自动化测试一"]')
    # 新增成功的业务系统的编辑按钮
    edit_new_sys_1_button = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="编辑"]')
    # 新增成功的业务系统的删除按钮
    delete_new_sys_1_button = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="删除"]')
    # 新增成功的业务系统的查看详情按钮
    view_new_sys_1_button = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="查看详情"]')
    # 删除业务系统的确定按钮
    delete_button = (By.XPATH, '// div[ @id="deleteModalTable"]//button[text()="确定"]')
    # 删除业务系统的取消按钮
    cancel_button = (By.XPATH, '// div[ @id="deleteModalTable"]//button[text()="取消"]')