# -*- coding: utf-8 -*-
# @Time     : 2019/6/6 9:33
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : do_file.py
# @Software : PyCharm
from Common import dir_config

class DoFile:
    # 打开远程获取的文本文件，取出name
    def get_file_name(self):
        f = open(dir_config.ftp_auto_text_01, encoding='utf-8')
        lines = f.read()
        res = lines[2] + lines[3] + lines[4]
        f.close()
        return res


if __name__ == '__main__':
    a=DoFile().get_file_name()
    print(a)