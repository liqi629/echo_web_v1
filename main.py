# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 11:25
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : main.py
# @Software : PyCharm
import pytest


pytest.main(["--html=TestResult/reports/report.html","--self-contained-html","--junitxml=TestResult/reports/report.xml"])
# pytest.main(["-m=smoke","--html=TestResult/reports/report.html","--junitxml=TestResult/reports/report.xml"])
# pytest.main(["-m=smoke","--html=TestResult/reports/report.html","--self-contained-html","--junitxml=TestResult/reports/report.xml"])