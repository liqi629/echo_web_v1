# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:06
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : dir_config.py
# @Software : PyCharm
import os

#
# print(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])
#
# print(os.path.realpath(__file__))
# print(os.path.split(os.path.realpath(__file__)))
# print(os.path.split(os.path.realpath(__file__))[0])
base_dir=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件路径

case_config_path=os.path.join(base_dir,'config','case.config')


#测试用例的路径
test_case_path=os.path.join(base_dir,'test_data','api.xlsx')

#html报告的路径
report_path=os.path.join(base_dir,'TestResult','reports','report.html')

#日志文件路径
logs_dir=os.path.join(base_dir,'TestResult','logs')
#截图文件路径
screenshot_dir=os.path.join(base_dir,'TestResult','imgs')

#数据库配置文件路径
db_config_path=os.path.join(base_dir,'config','db.config')
#从远程服务器下载文件存储路径
ftp_auto_text_01 = os.path.join(base_dir,'TestDatas','local_auto_text_01')


if __name__ == '__main__':
    print(case_config_path)
    print(test_case_path)
    print(report_path)
    print(logs_dir)
    print(ftp_auto_text_01)