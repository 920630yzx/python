# 1.字符串
char1 = 'abcdefg'
char2 = char1[3]
print(char2)
char3 = char1[3:]
print(char3)
print(char1[2:5])
print(char1[2:6])

# 2.循环打印字符串
for i in char1:  # 循环打印
    print(i)

# 3.判断字符a是否在char1中
if 'a' in char1:
    print('在')
else:
    print('不在')

# 4.判断字符串s_find是否在char1中,返回索引值   find()函数
s_find = 'def'
index = char1.find(s_find)  # 从右侧开始查找,找到第一次出现的位置就停止
print(index)

index = char1.find(s_find, 2, 5)  # 2.5规定了查找的范围,即在cde中找
print(index)

index = char1.rfind(s_find)  # 从右侧开始查找,只找到第一次出现的位置便停止
print(index)

# 5.字符串的替换   replace()函数
s = '012345678901234567890123456789'
s1 = s.replace('123', 'bitch')  # 将全部123替换成bitch,s不会改变
print(s)
print(s1)

s1 = s.replace('123', 'bitch', 2)  # 将全部123替换成bitch,s不会改变,这里表示只替换2次(从左起)
print(s1)

# 6.分割字符串   split()函数II
s = 'i am a apple'
s_new = s.split()  # 这里返回的是列表
print(s_new)

# 7.字符串大小写转换   capitalize()  upper()   lower()
s = 'i am a APPLE'
s_new = s.capitalize()  # 第一个字符串转成大写,其余小写
print(s_new)

s_new = s.upper()  # 全部转成大写
print(s_new)

s_new = s.lower()  # 全部转成小写
print(s_new)

s_new = s.title()  # 每个单词首字母全部转换成大写,其余小写
print(s_new)

# 8.字符串统计出现次数   count()函数
s_count = s.count('a')
print(s_count)

# 9.判断一个字符串是否以一个数开头或结尾：
s = '01234567890123456789'
if s.startswith('012'):  # 判断开头,s.startswith('012')会返回一个布尔值   print(s.startswith('012'))=True
    print('是')
else:
    print('否')

if s.endswith('789'):
    print('是的')
else:
    print('不是的')

# 10.判断字符串可否转换成数字：  isdigit()函数,返回布尔值
x = input('请输入')
if x.isdigit():  # 如果输入不是数字,自动退出
    print(float(x)**3)
else:
    print('不是数字')

















