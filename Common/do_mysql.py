# -*- coding: utf-8 -*-
# @Time     : 2019/5/29 14:13
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : do_mysql.py
# @Software : PyCharm
import pymysql
class DoMysql:
    def do_mysql(self,sql):
        # 1：根据登录信息  去登录数据库 产生一个数据库连接
        db = pymysql.connect(host='172.16.12.28',
                             port=3306,
                             user='root',
                             passwd='root',
                             db='echod')
        # 2：产生一个游标  可以获取数据库操作权限
        cursor = db.cursor()
        # 3:利用游标 进行操作
         # sql语句
        cursor.execute(sql)  # 执行sql
        # 获取结果：1）获取单条   2）获取多条
        # res=cursor.fetchone() #单  返回的是一个元组
        res = cursor.fetchall()  # 多  返回的是一个嵌套元组的列表
        # 关掉游标 关掉连接
        cursor.close()
        db.close()
        return res
    #删除数据表的内容
    def deletc_data(self,):
        db = pymysql.connect(host='172.16.12.28',
                             port=3306,
                             user='root',
                             passwd='root',
                             db='echod')
        cursor = db.cursor()
        cursor.execute('DELETE FROM AUTO_test_02')
        #commit()方法：在数据库里增、删、改的时候，必须要进行提交，否则插入的数据不生效。
        db.commit()
        cursor.close()
        db.close()
    def select_table_1(self):
        return self.do_mysql('select * from AUTO_test_01')

    def select_table_2(self):

        return self.do_mysql('select * from AUTO_test_02')
if __name__ == '__main__':
    # sql = 'select * from AUTO_test_01'  # sql语句
    # res = DoMysql().do_mysql(sql)
    # print("数据库的查询结果是：{0}".format(res))
    sql2 = 'DELETE FROM AUTO_test_02'
    DoMysql().deletc_data(sql2)
    print(DoMysql().select_table_1('select * from AUTO_test_02'))