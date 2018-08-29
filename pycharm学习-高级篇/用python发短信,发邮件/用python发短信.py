'''
1.接口类型：互亿无线触发短信接口；支持发送验证码短信；订单通知短信
2.账户注册：请通过http://www.ihuyi.com/注册,有50条免费短信
3.个人注册账户：18161280526 密码：920630yzx
APIID：C38547499
APIKEY：85242c9163ea5c65c4b80cfdb6082acd
4.注意事项：文档查看;请使用apiID和APIkey(登陆，用户中心---》验证码短信通知---》
获取apiID和 APIKEY)
host = 106.ihuyi.com (host需要以这个开头)
uri= webservice/sms.php?method=Submit'''

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib

# host = "106.ihuyi.com"  #定义主机
# sms_send_uri = "/webservice/sms.php?method=Submit" #发送的地址,请求的地址
# account = "C38547499"  #这里需要填写自己的APIID ！！！
# password = "85242c9163ea5c65c4b80cfdb6082acd"  #这里需要填写自己的密码 ！！！
#
# #发送短信：
# def send_sms(text,mobile):   #text表示:发送的文本;mobile表示发送的手机号
#     params = urllib.parse.urlencode( {'account':account,'password':password,'content':text,'mobile':mobile,'format':'json'})   #解析内容
#     headers = {"Content-type": "application/x-www-from-urlencoded",
#                "Accept": "text/plain"}   #设置请求头
#     conn = http.client.HTTPConnection(host, port=80, timeout=20)  #创建一个连接http连接；主机，端口 80   ；timeout = 20
#     conn.request("POST", sms_send_uri, params, headers)   #发送请求request(),获取响应;sms_send_uri是请求的地址
#     response = conn.getresponse()   #获取响应，得到对应的响应码
#     response_str = response.read()   #读取数据read  readline   readlines
#     conn.close()   #关闭连接
#     return response_str   #返回数据
#
# if __name__ == "__main__":
#     mobile = "18161280526"
#     text = "你的验证码是：772233.请不要把验证码给其他人"
#     print(send_sms(text,mobile))

'''
结果出现以下数字表示：
0	提交失败
2	提交成功
400	非法ip访问
401	帐号不能为空
402	密码不能为空
403	手机号码不能为空
4030	手机号码已被列入黑名单
404	短信内容不能为空
405	用户名或密码不正确
4050	账号被冻结
4051	剩余条数不足
4052	访问ip与备案ip不符
406	手机格式不正确
407	短信内容含有敏感字符
4070	签名格式不正确
4071	没有提交备案模板
4072	短信内容与模板不匹配
4073	短信内容超出长度限制
408	您的帐户疑被恶意利用，已被自动冻结，如有疑问请与客服联系。'''






# 接口类型：互亿无线触发短信接口，支持发送验证码短信、订单通知短信等。
# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
# 注意事项：
# （1）调试期间，请用默认的模板进行测试，默认模板详见接口文档；
# （2）请使用APIID（查看APIID请登录用户中心->验证码短信->产品总览->APIID）及 APIkey来调用接口；
# （3）该代码仅供接入互亿无线短信接口参考使用，客户可根据实际需要自行编写；

#APIID：C19491045
#APIKEY：487de5b5d7c3ff17cc4830fdf7f23c9c

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import http.client
import urllib
import random

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C38547499"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "85242c9163ea5c65c4b80cfdb6082acd"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "18161280526"
    text = "您的验证码是：888888。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))



