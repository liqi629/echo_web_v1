# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 9:58
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : readme.py
# @Software : PyCharm
'''

Common——公共代码
        BasePage——Web页面的常用操作，元素等待、查找元素、点击、获取文本、获取属性、切换窗口、截图等
        dir_config——目录配置
        logger——自定义日志格式
        send_email——配置发送邮件
PageLocators——元素定位
PageObjects——页面对象，各个页面需要测试的操作步骤
TestResult——测试结果输出目录
         imgs
        logs
        reports
TestCase——测试用例，按照页面新建不同的py
        test_login
        conftest:pytest.fixture，用于 会话、类、用例的初始操作设计
TestDatas——测试数据
        Common_Datas——存放公用的测试数据
main——执行文件
'''