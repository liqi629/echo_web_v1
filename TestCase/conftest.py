# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:40
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : conftest.py
# @Software : PyCharm
import pytest
from selenium import webdriver
from TestDatas import Common_Datas as CD
from PageObjects.login_page import LoginPage
from TestDatas import login_datas as ld
from Common.login import login
driver=None

@pytest.fixture(scope="session",autouse=True)
def mySession():
    print ("============session级别的会话=====开始=====================")
    yield
    print ("============session级别的会话=====结束=====================")
@pytest.fixture(scope="class")
def set_class():
    global driver
    print("============整个测试类只执行一次的前置======================")
    # 打开浏览器
    # driver = webdriver.Chrome()
    #谷歌无头模式
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options)
    #火狐无头模式
    # options = webdriver.FirefoxOptions()
    # options.add_argument('-headless')
    # driver = webdriver.Firefox(options=options)
    # 设置全屏
    driver.maximize_window()
    lp = LoginPage(driver)
    # 打开目标网页
    driver.get(CD.login_url)
    yield [driver,lp]  # 关键字隔开前置、后置    后面空格[返回值]
    driver.quit()
    print("============整个测试类只执行一次的后置======================")
# @pytest.fixture()
@pytest.fixture(scope="class")
def set_class_home():
    global driver
    print("============整个测试类只执行一次的前置======================")
    # 打开浏览器
    # driver = webdriver.Chrome()
    # #谷歌无头模式
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')#谷歌文档提到需要加上这个属性来规避bug
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options)
    #火狐无头模式
    # options = webdriver.FirefoxOptions()
    # options.add_argument('-headless')
    # driver = webdriver.Firefox(options=options)
    # 设置全屏
    driver.maximize_window()
    lp = LoginPage(driver)
    # 打开目标网页
    driver.get(CD.login_url)
    lp.login(ld.sucess_data["user"],ld.sucess_data["pwd"])
    lp.switch_alert()
    yield [driver,lp]  # 关键字隔开前置、后置    后面空格[返回值]
    driver.quit()
    print("============整个测试类只执行一次的后置======================")
@pytest.fixture()
def case_login():
    global driver
    print("============测试类中每个测试用例都执行一次的前置============")

    yield  # 关键字隔开前置、后置    后面空格[返回值]
    # 后置
    driver.get(CD.login_url)
    print("============测试类中每个测试用例都执行一次的前置============")
@pytest.fixture()
def case_home():
    global driver
    print("============测试类中每个测试用例都执行一次的前置============")

    yield  # 关键字隔开前置、后置    后面空格[返回值]
    # 后置

    print("============测试类中每个测试用例都执行一次的前置============")
@pytest.fixture()
def case_designer():
    global driver
    print("============测试类中每个测试用例都执行一次的前置============")
    driver.get(CD.designer_url)
    yield  # 关键字隔开前置、后置    后面空格[返回值]
    # 后置

    print("============测试类中每个测试用例都执行一次的前置============")
# @pytest.fixture()
# def case_login():
#     global driver
#     print("============测试类中每个测试用例都执行一次的前置============")
#     # 打开浏览器
#     driver = webdriver.Firefox()
#
#     # 设置全屏
#     driver.maximize_window()
#     lp = LoginPage(driver)
#     # 打开目标网页
#     driver.get(CD.login_url)
#     yield [driver,lp]  # 关键字隔开前置、后置    后面空格[返回值]
#     # 后置
#     driver.quit()
#     print("============测试类中每个测试用例都执行一次的前置============")
@pytest.fixture()
def sete():
    global driver
    print("============测试类中每个测试用例都执行一次的前置============")

    # 打开浏览器
    # driver = webdriver.Firefox()
    #
    # # 设置全屏
    # driver.maximize_window()
    # lp = LoginPage(driver)
    # # 打开目标网页
    # driver.get(CD.login_url)

    yield [driver]  # 关键字隔开前置、后置    后面空格[返回值]
    # 后置
    driver.quit()
    print("============测试类中每个测试用例都执行一次的前置============")