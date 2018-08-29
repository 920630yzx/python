# 5.匹配边界
'''
字符     功能
^      匹配字符串开头
$      匹配字符串结尾
\b    匹配一个单词的边界
\B     匹配非单词的边界'''


# 案例：匹配邮箱,匹配正确的邮箱地址
# @163.com  4~20
import re
ret = re.match("[\w]{4,20}@163\.com$", "xiaoming@163.com").group()  # '\.'表示一个'.'；因为一个'.'表示匹配任意1个字符（除了\n）
print(ret)  # $来确定末尾,表示结束;如果对不上则会报错；例如："xiaoming@163.com123"就会报错

ret = re.match(r".*\bver\b", "bitchbitchbitch ver abc").group()  # \b表示匹配一个单词的边界
print(ret)
print('\n')



# 5.匹配分租
'''
字符                       功能
|                 匹配左右任意一个表达式，也即表示或者
(ab)              将括号中的一个字符作为分组
\num              引用分组num匹配到的字符串
(?p<name>)               分组起别名
（？p=name）      引用别名为name分组匹配到字符串'''

import re
# 案例1：匹配出0~100之间的数字
ret = re.match("[1-9]?\d", "08").group()
print(ret)  # ans:0

# ret = re.match("[1-9]?\d$", "08").group()  报错！！！
# print(ret)  报错！！！

ret = re.match("[1-9]?\d$", "8").group()
print(ret)  # ans:8

ret = re.match("[1-9]?\d$", "18").group()
print(ret)  # ans:18

ret = re.match("[1-9]?\d$|100", "100").group()  # |表示或者
print(ret)
print('\n')



# 案例2：同时匹配邮箱163 126 qq
qq = re.match("\w{4,20}@(163|126|qq).com$", "1031003790@qq.com").group()  # 这样就可以同时匹配163|126|qq了
print(qq)



# 案例3：匹配<html><h1>haha</h1></html>
ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<br>haha</br>")  # 注意/不是\
print(ret.group())



# 案例4：匹配"<html><h1>haha</h1></html>"
ret = re.match(r"<(\w*)><(\w*)>.*</(\w*)></(\w*)>", "<html><h1>haha</h1></html>")  # 注意(\w*)也可不用括号
print(ret.group())




# 案例5：匹配"<html><h1>haha</h1></html>"
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>","<html><h1>haha</h1></html>")  # 简写方式,\1表示第一个,\2表示第二个
print(ret.group())