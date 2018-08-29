# 1.正则表达式：
'''
在python中需要通过正则表达式对字符串进行匹配，内置模块，直接导入就可以使用match
说明：re.match函数用来进行正则表达式匹配检查方法.如果字符串匹配成功,match返回匹配对象（Match object）,反之返回None.   注意：None不是空字符串
同时，该匹配方式匹配的是字符串的开头！！！

# re模块的使用过程：
1.导入re模块:import re
2.使用match方法进行匹配操作
reslut = re.match(参数1，参数2)   参数1：正则表达式,匹配规则  参数2：要匹配的字符串
3.如果上一步得到数据，group函数提取数据
reslut.gorup()'''

#1. re模块的操作
import re
reslut = re.match("虎王", "虎王-E75")  # "虎王-E75"是要匹配的字符串，"虎王"是匹配规则
print(reslut.group())  # ans：虎王；如果没有则返回none
print('\n')





# 2.表示字符
'''
正则表达式的单字符匹配:  需要注意re.match都是匹配开头
字符       功能
.     匹配任意1个字符（除了\n）
[]    匹配[]中列举的字符
\d    匹配十进制数字，即0~9
\D    匹配除十进制数字
\s    匹配空白    空格   tab键
\S    匹配非空白
\w    匹配单个字符   a~z   A `~ Z   0~9   下划线
\W    匹配非单词字符  非\w
\n	  匹配换行符  
\t 	  匹配制表符'''



#step1：匹配任意一个字符
ret = re.match(".", "W")
print('匹配任意一个字符:', ret.group())

ret = re.match(".", "wc")
print(ret.group())

ret = re.match(".", "好wc")
print(ret.group())
print('\n')


#step2:如果hello的首字母为小写h
ret = re.match("h", "hello")
print(ret.group())

ret = re.match("H", "Hello")  # 如果Hello的首字母为大写H
print(ret.group())
print('\n')

#step3：判断一个字符串是否以数字开头
ret = re.match("[0123456789]", "7hello")  # 匹配规则"[0123456789]"
print(ret.group())  # ans：7
ret = re.match("[0-9]", "7hello")
print(ret.group())  # ans：7
ret = re.match("\d", "7hello")   # \d    匹配数字，即0~9
print(ret.group())
print('\n')

#step4：匹配字符串
ret = re.match("嫦娥\d号", "嫦娥1号发射成功")
print(ret.group())
ret = re.match("嫦娥\d号", "嫦娥2号发射成功")
print(ret.group())
print('\n')