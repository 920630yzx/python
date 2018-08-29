# -*- coding: utf-8 -*-
"""
Created on Thu May 17 20:51:09 2018

作业可以提交到
码云
我们可以使用Urllib模块快速地爬取某一个网页，接下来将具体介绍：

1、https与http协议
2、urlopen与urlretrieve以及Request
3、网页状态码
@author: yq
"""
import urllib.request as r
#爬到内存中
r.urlopen('http://www.baidu.com').read().decode('utf-8','ignore')

f=r.urlopen('http://www.baidu.com')
#3、网页状态码
f.getcode()#打开网页的状态。网页可以访问
if f.getcode()==200:
    data=f.read().decode('utf-8','ignore')
    
#爬到硬盘中
r.urlretrieve('http://www.baidu.com','./baidu.html')


#爬到内存中--方式2
req=r.Request('http://www.baidu.com')#放入用户名和密码
f=r.urlopen(req)
f.getcode()










    


