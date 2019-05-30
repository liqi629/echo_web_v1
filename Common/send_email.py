# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:07
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : send_email.py
# @Software : PyCharm
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

#邮件发送的用户名和密码   常识：第三方授权码    pwd  为第三方授权码 不是邮箱密码
_user = "liqi_629@163.com"
_pwd = "helloemail163"

now = time.strftime('%Y-%m-%d_%H_%M_%S')#获取时间戳

class sendEmail:
    def send_email(self,email_to,filepath):
        #email_to 收件方
        #filepath 发送附件的地址
        #如名字所示 Multipart就是分多个部分
        msg = MIMEMultipart()
        msg["Subject"] = now+"李奇的测试报告"
        msg["From"] = _user
        msg["To"] = email_to

        #——这是文字部分——
        part = MIMEText("这次是自动化测试结果，请查收")
        msg.attach(part)

        #——这是附件部分——
        part = MIMEApplication(open(filepath,'rb').read())
        part.add_header('Content-Disposition','attachment',filename=filepath)
        msg.attach(part)
        s = smtplib.SMTP_SSL("smtp.163.com",timeout=30)
        s.login(_user,_pwd)#登录
        s.sendmail(_user,email_to,msg.as_string())
        s.close()

if __name__ == '__main__':
    sendEmail().send_email('liqi_629@163.com',"F:\py_web_v1\\test_result\\reports\\report.html")