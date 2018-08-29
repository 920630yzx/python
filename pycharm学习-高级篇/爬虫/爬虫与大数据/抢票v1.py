# -*- coding: utf-8 -*-
"""
Created on Tue May 29 21:16:19 2018

抢票的重点是，依次拿到12306的网络请求
然后依次请求12306即可。

@author: yq
"""
import urllib.request
import re
import ssl
import urllib.parse
import http.cookiejar
import datetime
import time
import json     
import sys   
import urllib.request as r


class LoginUser:
    def __init__(self,username,pwd,cardname,cardid,mobile):
        self.username = username#12306账户名密码
        self.pwd = pwd
        self.cardname = cardname#身份证信息
        self.cardid = cardid
        self.mobile = mobile
    
    def __str__(self):#可以直接print改对象
        return urllib.parse.urlencode({
                "username":self.username,
                "password":self.pwd,
                "appid":'otn'
                })
get=lambda url:r.urlopen(url).decode('utf-8','ignore')
class TickerControl:
    #初始化方法
    def __init__(self,loginUser:LoginUser):
        self.网络设置()
        self.loginUser = loginUser#购票的账号和身份证信息
        self.登陆用户()
    def 网络设置(self):
        '可以保存网路状态,启用cookies，设置浏览器代理'
        cjar=http.cookiejar.CookieJar()
        opener=r.build_opener(r.HTTPCookieProcessor(cjar))
        opener.addheaders=[('User-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0')]
        r.install_opener(opener)
        pass
    def 用户信息输入(self):
        
        pass
    def 登陆用户(self):
        print('验证码....')
        url='https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
        r.urlretrieve(url,'./tmp.png')
        #打开外部程序，sys.sys
        import os
        os.system('mspaint tmp.png')
        
        pngmap={"1":[39,43],"2":[110,41],"3":[182,41],"4":[259,36],
         "5":[38,115],"6":[111,113],"7":[183,113],"8":[255,112]}
        #answer=182%2C+40%2C+41%2C+114&rand=sjrand&login_site=E
        url='https://kyfw.12306.cn/passport/captcha/captcha-check'
        no=input('请输入验证码编号(例如1,是选择第一张图片,12是第一张和第二张):')
        #如果输入多个验证码，需要使用循环。。。。
        answer=''
        for i in list(no):
            answer=answer+str(pngmap[i][0])+","+str(pngmap[i][1])+","
            print(answer)
        answer=answer[:-1]
        print(answer)
        params=urllib.parse.urlencode({
                "answer":answer,
                "rand":'sjrand',
                "login_site":'E'
                }).encode('utf-8')
        req=r.Request(url,params)
        data=r.urlopen(req).read().decode('utf-8','ignore')
        print('验证图片结果：',data)
        
        print('登陆....')
        #TODO 
        pass
    
    def 订票(self):
        self.查询余票()
        self.预定()
        self.提交订单()
        self.座位确定()
        self.等待系统处理订单结果()
        self.可以支付()
    def 查询余票(self):
        pass
    def 预定(self):
        pass
    def 提交订单(self):
        pass
    def 座位确定(self):
        pass
    def 等待系统处理订单结果(self):
        pass
    def 可以支付(self):
        pass
#模板设计模式

        



