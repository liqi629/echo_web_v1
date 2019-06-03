# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:04
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : BasePage.py
# @Software : PyCharm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from Common import dir_config
import logging
from Common import logger
import time
'''
需要引入logger，才能使用自己定义好的日志
封装操作页面时候用的常用操作
'''
class BasePage:
    def __init__(self,driver):#必须外部传入driver  同一个driver经历多个页面
        self.driver=driver

    #等待元素可见
    def wait_eleVisible(self,loc,timeout=30,poll_frequency=0.5,model=None):
        '''
        :param loc: 元素定位表达式。元素类型，表达方式（元素定位类型，元素定位方法）
        :param timeout: 等待超时时间上限
        :param poll_frequency: 轮询周期
        :param model:等待失败时，截图操作，图片文件中需要显示的功能模块标注
        :return: None
        '''
        logging.info("{1}：等待元素可见：{0}".format(loc,model))
        try:
            start = time.time()
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.visibility_of_element_located(loc))
            end = time.time()
            logging.info("等待时长{0}：以秒为单位".format(round(end-start,2)))
        except:
            logging.error("等待元素可见失败。")
            #截图
            self.save_webImgs(model)
            raise
    #查找一个元素
    def get_Element(self,loc,model=None):
        logging.info("{1}：查找元素：{0}".format(loc, model))
        try:
            return self.driver.find_element(*loc)
        except:
            logging.error("查找元素失败。")
            # 截图
            self.save_webImgs(model)
            raise
    #输入操作
    def input_text(self,loc,text,model=None):
        #查找元素
        ele = self.get_Element(loc, model)
        #输入元素
        logging.info("{0}：在元素{1}中输入文本：{2}".format(model,loc,text))
        try:
            ele.send_keys(text)
        except:
            logging.error("输入操作失败。")
            # 截图
            self.save_webImgs(model)
            raise
    #鼠标悬浮
    def hover_element(self,loc,model=None):
        #查找元素
        ele = self.get_Element(loc, model)
        #鼠标悬浮在元素
        logging.info("{0}:元素：{1}鼠标悬停事件".format(model, loc))
        try:
            AC(self.driver).move_to_element(ele).perform()
        except:
            logging.error("鼠标悬停操作失败。")
            # 截图
            self.save_webImgs(model)
            raise

    #点击操作
    def click_element(self,loc,model=None):
        #找元素再点击
        ele = self.get_Element(loc, model)
        #点击操作
        logging.info("{0}:元素：{1}点击事件".format(model,loc))
        try:
            ele.click()
        except:
            logging.error("元素：{0}点击事件失败".format(loc))
            self.save_webImgs(model)
            raise
    #清除操作
    def clear_input_text(self,loc,model=None):
        #找元素再清除
        ele = self.get_Element(loc, model)
        logging.info("{0}：清除元素：{1}".format(model, loc,))
        try:
            ele.clear()
        except:
            logging.error("清除失败")
            self.save_webImgs(model)
            raise
    #获取文本内容
    def get_text(self,loc,model=None):
        #找到元素
        self.wait_eleVisible(loc)
        ele = self.get_Element(loc,model)
        #获取元素的文本内容
        logging.info("{0}:获取元素:{1}的文本内容".format(model,loc))
        try:
            text=ele.text
            logging.info("{0}:元素:{1}的文本内容为:{2}".format(model, loc,text))
            return text
        except:
            #捕获异常到日志
            logging.error("获取元素:{0}的文本内容失败。".format(loc))
            #截图
            self.save_webImgs(model)
            #抛出异常
            raise
    #获取元素属性
    def get_element_attribuute(self,loc,attr_name,model=None):
        #找到元素
        ele = self.get_Element(loc, model)
        #获取元素属性
        logging.info("{0}:获取元素：{1}的属性：{2}".format(model,loc,attr_name))
        try:
            value=ele.get_attribute(attr_name)
            logging.info("{0}:元素：{1}的属性：{2}值为：{3}".format(model,loc,attr_name,value))
            return value
        except:
            logging.error("获取元素：{0}的属性：{1}失败，异常信息".format( loc, attr_name))
            self.save_webImgs(model)
            raise
    #截图
    def save_webImgs(self,model=None):
        #filepath=制定的图片保存目录/model(页面功能名称)_当前时间到秒.png
        filepath=dir_config.screenshot_dir+\
                 "/{0}_{1}.png".format(model,time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()))
        try:
            self.driver.save_screenshot(filepath)
            logging.info("截屏成功,图片路径为{0}".format(filepath))
        except:
            logging.error("截屏失败")
    #iframe切换
    def switch_iframe(self,frame_refer,timeout=30,poll_frequency=0.5,model=None):
        #等待iframe存在
        logging.info("iframe切换操作：")
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.frame_to_be_available_and_switch_to_it(frame_refer))
            time.sleep(0.5)
            logging.info("切换成功")
        except:
            logging.error("iframe切换失败！")
            self.save_webImgs(model)
            raise
        #切换回初始还没有完善
        # self.driver.switch_to_default_content()

        #切换==index、name\id\WebElement
    #alert切换
    def switch_alert(self,timeout=30,poll_frequency=0.5,model=None):
        '''
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :param timeout:
        :param poll_frequency:
        :param model:
        :return:
        '''
        try:
            result = EC.alert_is_present()(self.driver)
            if result:
                msg = result.text
                logging.info("alert出现，内容为：{0}".format(msg))
                result.accept()
                logging.info("alert已经关闭")
                return msg
            else:
                logging.info("未弹出alert")

        except:
            logging.error("alert切换失败！")
            self.save_webImgs(model)
            raise
    #获取窗口句柄
    def current_handles(self):
        current_handles = self.driver.window_handles
        return current_handles
    #窗口切换==如果是切换到新窗口，new，如果是回到默认窗口，default。切换前，在新窗口打开前获取handles
    def switch_window(self,name,current_handles=None,timeout=30,poll_frequency=0.5,model=None):
        '''
        :param name: new代表最新打开的一个窗口。default代表第一个窗口。其他的值表示为窗口的handles
        :param current_handles:
        :param timeout:
        :param poll_frequency:
        :param model:
        :return:
        '''
        try:
            if name =="new" and current_handles is not None:
                logging.info("切换到最新打开的窗口")
                WebDriverWait(self.driver,timeout,poll_frequency).until(EC.new_window_is_opened(current_handles))
                window_handles = self.driver.window_handles#获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif name =="default":
                logging.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
                #self.driver.switch_to_default_content()
            else:
                logging.info("切换到指定handles")
                self.driver.switch_to.window(name)
        except:
            logging.error("切换失败")
            self.save_webImgs(model)
            raise
