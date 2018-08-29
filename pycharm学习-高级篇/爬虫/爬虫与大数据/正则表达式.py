# -*- coding: utf-8 -*-
"""
Spyder Editor
ctrl+   方法字体
This is a temporary script file.
python 2020从上海开始纳入小学教材
       高考 python编程
       AI人工智能
       工作：python开发
       zhaopin.com 搜索python爬虫
python爬虫(10k~43k)
    初级：10000-15000
    中高级：15K~43K
    
爬虫：采集互联网信息，代替人工。    


信息筛选-正则表达式
re.compile(正则表达式).findall(下载的数据中)

执行代码ctrl+回车
"""

import re
"""
正则表达式：'yu'
信息数据：'aliyunedu'
\w   可以代表任意的[英文字母、
\n   代表换行

"""
re.compile('yu').findall('aliyunedu')

re.compile('ya').findall('aliyunedu')

#匹配换行 \n
data='''aliyun
edu'''

re.compile('yun\n').findall(data)


re.compile('\w').findall('、')

#u89787 寻找目标
re.compile('\w').findall('aliyu89787nedu')



"""
正则表达式中的字符代表：
普通字符	正常匹配
\n			匹配换行符  
\t 			匹配制表符
\w 			匹配字母、数字、下划线word
\W 			匹配除字母、数字、下划线
\d 			匹配十进制数字digital
\D 			匹配除十进制数字
\s 			匹配空白字符
\S 			匹配除空白字符
[ab89x]		原子表，匹配ab89x中的任意一个
[^ab89x]		原子表，匹配除ab89x以外的任意一个字符
"""
re.compile('[ab89x]').findall('a')

re.compile('\w897').findall('aliyu89787nedu')


re.compile('t\w\w\we').findall('><title>百度一下，你就知道 </title><style ')
re.compile('t...e').findall('><title>百度一下，你就知道 </title><style ')
re.compile('^t...e').findall('><title>百度一下，你就知道 </title><style')
re.compile('.tyle$').findall('><title>百度一下，你就知道 </title><style')


"""
信息筛选---------正则表达式、想要字母、数字、以....开始的字符
基础2：
.	匹配除[换行]外任意一个字符
^	匹配开始位置
$	匹配结束位置
*	前一个字符出现0\1\多次 
?	前一个字符出现0\1次
+	前一个字符出现1\多次
{n}	前一个字符恰好出现n次
{n,}	前一个字符至少n次
{n,m}前一个字符至少n，至多m次 
|	模式选择符或
()	模式单元，通俗来说就是：[想提取出什么内容]，就在正则中用小括号将其括起来
"""
re.compile('<title>.*</title>').findall('><title>百度一下，你就知道了</title><style')

re.compile('<title>(.*)</title>').findall('><title>百度一下，你就知道了</title><style')

re.compile('<a href=http://www.hao123.com target=_blank class=mnav>(.*)</a>').findall('<a href=http://www.hao123.com target=_blank class=mnav>hao123</a>')


re.compile('<title>(.?)</title>').findall('><title>百111</title><style')
re.compile('<title>(.*)</title>').findall('><title>百</title><style')
re.compile('<title>(.{4})</title>').findall('><title>百度一下</title><style')
re.compile('<title>(.{4,})</title>').findall('><title>百度一下</title><style')


"""
高级匹配
贪婪模式，懒惰模式。。。。。
"""
re.compile('py(.*)on').findall('pythonpythonpython')

#提取列表，淘宝商品列表，招聘岗位列表，百度搜索列表
re.compile('py(.*?)on',re.S).findall('python   python   python')

"""
re.S 代表可以匹配多行的数据内容的
"""
x='''pytho
n
kdjfon'''
re.compile('py.*?on',re.S).findall(x)

x='''尽在智联招聘</title>
<META content
'''
re.compile('tle><ME').findall(x)

re.compile('A',re.I).findall('abc')#ignore忽略







