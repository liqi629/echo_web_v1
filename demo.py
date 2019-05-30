# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 11:05
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : demo.py
# @Software : PyCharm
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
    # 设置全屏
# driver.maximize_window()

    # 打开目标网页
driver.get("http://172.16.12.28:18080/echod_manager/V2/login.jsp")

#输入账号
driver.find_element_by_xpath('//input[@id="name"]').send_keys("admin")
#输入密码
driver.find_element_by_xpath('//input[@id="inputPassword"]').send_keys("admin")
#点击登陆
driver.find_element_by_xpath('//a[@id="login"]').click()
#处理弹窗
time.sleep(5)

WebDriverWait(driver,2).until(EC.alert_is_present())
alert = driver.switch_to.alert
#打印文本
print(alert.text)
#关闭弹窗——接受，ok
alert.accept()

driver.refresh()
time.sleep(2)
#直接进入设计器
driver.quit()
# driver.get("http://172.16.12.28:18080/echod_manager/V2/designer/designer.jsp")