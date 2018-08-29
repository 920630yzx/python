# 3.原始字符串
import re
mm = "c:\\a\\b\\c"
print(mm)

ret = re.match("c:\\\\", mm).group()  # c:\\\\转义后表示c:\\；正好对应mm中的c:\\
print(ret)  # 输出后需要再转义一次为：c:\
ret = re.match("c:\\\\a", mm).group()
print(ret)
# ret = re.match("c:\\a",mm).group()  # 报错！
# print(ret)
ret = re.match(r"c:\\a", mm).group()  # pyhton字符串中前面加上r,表示原生字符串,不用转义
print(ret)
print('\n')


# 4.表示数量
'''
匹配多个字符串的格式：
字符        功能
*      匹配前一个字符出现0次或者无限次;可有可无
+      匹配前一个字符出现1次或者无限次;至少一次
？     匹配前一个字符出现1次或者0次;要么有1次 要么没有
{m}    匹配前一个字符出现m次
{m,}   匹配前一个字符至少出现m次
{m,n}  匹配前一个字符出现的从m到n次'''

# step1:匹配出,一个字符串中第一个字母为大写,后面都是小写字母（可有可无）
import re
ret = re.match("[A-Z][a-z]*", "Ajfsdahsadfqwiweyue3hbdbnj")  # [A-Z]表示第一个字母；[a-z]表示第二个字母，*表示可有可无,可以出现0次到n次
print(ret.group())

# step2：匹配变量名是否有效  也就是：标识符为数字,字母,下划线,数字不能开头
ret = re.match("[a-zA-Z_][\w_]*", "_name1")  # [a-zA-Z_]表示a-z+A-Z+_(下划线)；\w表示匹配单个字符   a~z  A `~ Z  0~9
print(ret.group())

# step3：匹配0~99之间的数字，最高位不为0
ret = re.match("[1-9]?[0-9]", "1000000000").group()
print(ret)