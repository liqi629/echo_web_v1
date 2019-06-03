# -*- coding: utf-8 -*-
# @Time     : 2019/6/3 16:21
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : back.py
# @Software : PyCharm
# 多表配置
def table_config(self):
    self.add_source()
    self.add_target_source()
    # 点击目标
    self.wait_eleVisible(loc.target_source)
    self.click_element(loc.target_source)
    # 点击映射关系
    self.click_element(loc.map)
    # 等待两个表出现
    self.wait_eleVisible(loc.source_title)
    self.wait_eleVisible(loc.out_source_title)
    # 点击多表配置
    self.wait_eleVisible(loc.table_config)
    self.click_element(loc.table_config)
    self.wait_eleVisible(loc.config_button)
    self.click_element(loc.config_button)
    time.sleep(0.5)
    # 调用函数保存映射
    self.save_map()
    # 刷新页面
    # self.driver.refresh()
    time.sleep(5)


# 判断多表配置后 映射连线是否出现
# 使用js调用 返回非空[]
def is_map_line(self):
    logging.info("调用js语句")

    js = 'graph.model.getCell(1).children.filter(function(e,idx){return e.edge })'
    res = self.driver.execute_script(js)
    if res != []:
        logging.info("调用js返回的内容是：{0}".format(res))
        return True
    else:
        logging.info("调用js语句失败")
        return False




