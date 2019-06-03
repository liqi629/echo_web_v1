# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 16:35
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : demo_2.py
# @Software : PyCharm

#
# abc="hel;askdasd"
# if abc:
#     print("asd")
# else:
#     print("fdasfdasfd")
from TestDatas import designer_datas
#
# print(designer_datas.sucess_toast)
from Common.do_mysql import DoMysql
select_sql_1 = 'select * from AUTO_test_01'
select_sql_2 = 'select * from AUTO_test_02'
res_1 = DoMysql().do_mysql(select_sql_1)
# res_2 = DoMysql().do_mysql(select_sql_2)
# DoMysql().deletc_data('DELETE FROM AUTO_test_02')
print(res_1)