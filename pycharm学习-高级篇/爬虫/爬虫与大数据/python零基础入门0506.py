# -*- coding: utf-8 -*-
"""
Created on Sun May  6 19:51:32 2018
python大数据

python Anaconda(spyder)开发工具
ctrl+  方法
招聘网站地址：
https://sou.zhaopin.com/jobs/searchresult.ashx?
jl=北京&kw=python开发&sm=0&isfilter=1&p=1&sf=8001&st=100000
python相关职位
python开发
    python爬虫、python数据分析、python大数据、python后端
    python人工智能
    薪资：>8K
前期上直播课 
print功能：
1.Python 3.6.2 版本  
2.运行代码：ctrl+enter
3.print打印信息
4.信息里面包含   \n换行(line)  \t缩进(tab)
变量a,b,c:
int整数类型
float小数类型(浮点数)
str字符类型
list列表类型
@author: yq
"""
print("python你好")
print("1.北京天气\n2.其它城市天气\n3.未来五天天气\n4.设置")
print("python\t你好")

x = 3  
y = 4
z = x+y
x,y = -1,-2

a = 1.1
print("a的值是",a)
print(a)

a = "男"
print(a)


print(type(a))

""" """
a = [60,80,70,99]
print(a[0])
print(a[1])

"""
遇到错误，可以适当看下翻译
https://translate.google.com/
数字类型可以相加，字符类型是想连接的

可以从字符类型转换为整数类型
"""
a1 = "11"
b1 = "12"
c1 = a1+b1

a2 = int(a1)
b2 = int(b1)
c2 = a2+b2

a3 = int("123")

a4 = 1.1

a5 = float("1.11111")
""" 
= 赋值 ,例如a = 3
== 判断是否相等，例如1==2,
《第一次亲密接触》  痞子蔡
如果我有一千万，我就买一栋房子。
我有一千万吗？没有，所以我仍然没有房子。
"""
print("请选择菜单1.北京天气\n2.其它城市天气")
no = -1
if no==1:
    print("你选择了1")


money = 500
if money >= 1000:
    print("我就买一栋房子")
else:
    print("没有，所以我仍然没有房子。")

"""
加入小云考试了，现在要给判断级别
(多选一,选择到了直接退出选择)
大于80 优秀
大于70 中等
大于60 及格
小于60 不及格
"""
a = 70
if a>=80:
    print("优秀")
elif a>=70:
    print("中等")
elif a>=60:
    print("及格")
else:
    print("不及格")

"""
答题环节1
重点解释：
1.多选一结构
2.从上往下做选择，只有上面不成立的情况下，才会往下执行
"""
a = 70
if a>=60:
    print("优秀")
elif a>=70:
    print("中等")
elif a>=80:
    print("及格")
else:
    print("不及格")

"""
答题环节2
重点解释：
and 并且
a大于80分 并且 a小于100分
"""
a = 70
if a>=80 and a<=100:
    print("优秀")
elif a>=70:              #"""a<80 and 多此一举"""
     print("中等")
elif a>=60:              #"""a<70 and 多此一举"""
     print("及格")
else:
    print("不及格")

"""
下集预告：
假如A同学喜欢上了B同学，要送1000多玫瑰花给B同学
有一个同学一次性送了100万朵玫瑰花，请问他是怎么做到的？
"""
print("送B同学第1朵玫瑰花")
print("送B同学第2朵玫瑰花")
print("送B同学第3朵玫瑰花")
print("送B同学第4朵玫瑰花")
for i in range(1,1000001):
    print("送B同学第",i,"朵玫瑰花")

"""
1.建议大家都敲一下
2.尽量不要用python来做数学题目
3.python基础学习时间7小时
4.python爬虫工程师，1~2月完成
5.如果有很多问题需要咨询


"""













































