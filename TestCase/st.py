# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 17:13
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : st.py
# @Software : PyCharm
from PageObjects.home_page import HomePage as hp
import pytest
@pytest.mark.usefixtures("set_class_home")#整个套件setupClass
@pytest.mark.usefixtures("case_home")#整个套件setupClass
class TestHome:
    #页面切换——数据源管理
    def test_home_to_data_source(self,set_class_home):
        # 操作步骤：点击数据源管理——判断是否切换到数据源管理页——退出iframe（退出操作进行优化？？？）
        hp(set_class_home[0]).click_data_source()
        msg = hp(set_class_home[0]).is_data_source()
        set_class_home[0].switch_to.default_content()
        assert msg==True
    #页面跳转——设计器
    # @pytest.mark.flaky(reruns=5, reruns_delay=1)
    def test_home_jump_designer(self,set_class_home):
        #操作步骤
        hp(set_class_home[0]).into_designer()





