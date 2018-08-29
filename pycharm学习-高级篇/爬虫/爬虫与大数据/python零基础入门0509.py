# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:03:56 2018

@author: yq
"""
"""
1.建议大家都敲一下
2.尽量不要用python来做数学题目
3.python基础学习时间7小时
4.python爬虫工程师，1~2月完成
5.如果有很多问题需要咨询

循环
for当什么时候  0~100
range 范围,区间
"""
ls = [1,2,3,-1]
print(ls[0],ls[1],ls[2],ls[3])

for i in range(0,4):#[0,4)
    print(i)

a = '我'+str(1)

for i in range(0,100):
    print('送第'+str(i)+'朵玫瑰花')
    
for i in ls:
    print(i)

"""
班上4位同学的成绩
[99,80,91,30]
求最大数:
求最小数:
给成绩排序(大到小):
查看函数内部参数说明：ctrl+i   info
"""
ls = [99,80,91,30]
a = max(ls)
b = min(ls)
ls1 = sorted(ls)#30, 80, 91, 99
ls2 = sorted(ls,reverse=True)

aa = 3>4#布尔类型， False,True
bb = 3>1

"""
console控制台：错误信息，提示，输入内容。
---------------
-------------------------
------------------------------
----------------------------
-----------------------------
"""
ls = [15,10,20,18,19]#5天天气的温度
print('-'+1)
print('-'*15)

for i in ls:
    print(i*'-')

"""
读取记事本文件
神武门(玄武门 因为康熙叫玄烨 所以玄字不能再使用)
"""
read = open('./areaid_f.txt')
ls = read.readlines()

"""
http://api.openweathermap.org/data/2.5/weather?q=beijing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996
https://www.baidu.com/
网页、本地路径也叫url(http: https: file:///)
建议使用谷歌浏览器,F12 程序员的工具
import导入，导入联网的功能包
lib包
request请求网络数据
由于....计算机最开始不支持中文
最开始只支持字母标点符号
a
'我'

"""
url = 'http://api.openweathermap.org/data/2.5/weather?q=beijing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
import urllib.request as r

read = r.urlopen(url)
data = read.read()#如果str字符串的内容过长，有可能不会在内存中显示
print(data)

a=[1,1]
"""
dict字典   wo-100---我
          a-1------啊

"""
msg={'from':'qqyu','name':'潇潇','phone':'15038363546','neirong':'你在干嘛？'}

print('潇潇同学回家了，立马拆开短信：')
print(msg['from'])
msg['neirong']

ls = [70,71,79]

msg = {'name':'刘浩','neirong':[70,71,79]}

print(msg['neirong'])

"""
给刘浩同学发送最近三个月的体重报告
第一次
[70,71,79]
第二次
[70,71,81]
第三次：
[71,71.5,85]
"""

msg = {'name':'刘浩','neirong':[70,71,79]}

d = {"name":"qqyu","address":'北京海淀'}

ls = [1,2,3,'abc',{}]#


ls1 = [{}]#

s = '101010100	beijing	北京	beijing	北京	beijing	北京	china	中国'

ls = s.split()#一个字符分割成多个，就是一个列表list

print(ls[2])
"""
1.编写代码题：
读取areaid_f.txt文件
打印ls[6]是 黑龙江 的信息全部打印出来
2.编写代码 打印温度折线图
00000
00000
00000
10000
11001
11001
11001
11011
11011
11011
11011
11111
学习建议：
1.把讲过的代码先练习，
2.用自己的想法敲出来
3.开始思考代码题

"""



















