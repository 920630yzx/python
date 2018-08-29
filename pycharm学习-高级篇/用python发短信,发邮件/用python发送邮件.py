#smtp模块：用于邮件的发送
#163/126/qq  要求开启smtpde 权限
#模块：邮件文本  email   MIMEText

import user
from email.mime.text import MIMEText
import smtplib  #需要导入法邮件的库
SMTPServer = "smtp.163.com" #设置SMTP的服务器,这里是网易邮箱   个人注册的网易邮箱：18161280526@163.com   密码：920630yzx
#SMTPServer = "smtp.qq.com" #设置SMTP的服务器,这里是qq邮箱

sender = user.SENDER  #设置发邮件的地址(写给谁的地址),字符串的格式书写，已在user中写好
passwd = user.PASSWD #设置发送者邮箱的密码(他的密码),字符串的格式书写，已在user中写好

message = "你是一个好人！" #设置发送的内容！！！可以更换
msg = MIMEText(message) #转换成邮件的文本
msg["subject"] = "来自帅哥的问候" #标题！！！可以更换
msg["from"] = sender  #发送者
mailServer = smtplib.SMTP(SMTPServer,25) #创建SMTP服务器
mailServer.login(sender,passwd) #登陆邮箱
mailServer.sendmail(sender,[user.SENDER],msg.as_string()) #发送邮件sendmail()
mailServer.quit()  #退出邮箱






















