# -*- coding: utf-8 -*-
# @Time     : 2019/6/5 16:48
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : remote.py
# @Software : PyCharm
import paramiko
import logging
from Common import logger
from Common import dir_config
class Remote:
    #获取远程 文件到本地
    def get_file(self,ip,port,username,pwd,remote,local):
        '''
        :param ip: 远程服务器IP地址
        :param port: ftp服务端口
        :param username: 登录服务器的用户名
        :param pwd: 登录服务器的用户名
        :param remote: 远程文件所在目录
        :param local: 下载到本地的目录地址
        :return:
        '''
        # 实例化一个transport对象
        transport = paramiko.Transport((ip,port))
        # 建立连接
        transport.connect(username=username, password=pwd)
        # 实例化一个 sftp对象,指定连接的通道
        sftp = paramiko.SFTPClient.from_transport(transport)
        # LocalFile.txt 上传至服务器 /home/fishman/test/remote.txt
        # sftp.put('LocalFile.txt', '/home/fishman/test/remote.txt')
        # 将LinuxFile.txt 下载到本地 自定义文件路径中
        sftp.get(remote,local )
        logging.info("远程文件已经下载到本地")
        transport.close()
    #连接远程服务器，进行命令操作
    def cmd(self,ip,port,username,pwd,cmd):
        # 实例化一个transport对象
        transport = paramiko.Transport((ip, port))
        # 建立连接
        try:
            logging.info("准备建立连接")
            transport.connect(username=username, password=pwd)
            # 将sshclient的对象的transport指定为以上的transport
            ssh = paramiko.SSHClient()
            ssh._transport = transport
            # 执行命令，和传统方法一样
            logging.info("准备执行命令:{0}".format(cmd))
            stdin, stdout, stderr = ssh.exec_command(cmd)
            logging.info(stdout.read().decode())
            # 关闭连接
            transport.close()
            logging.info("连接已经关闭")
        except:
            logging.info("连接失败")
if __name__ == '__main__':
    # Remote().get_file('172.16.12.28',22,'root','yoyosys','/user/liqitest/auto_text_01',dir_config.ftp_auto_text_01)
    #删除文本内容
    Remote().cmd('172.16.12.28',22,'root','yoyosys','> /user/liqitest/auto_text_01')
