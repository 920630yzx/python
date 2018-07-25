"""
第1题：获取每一个单词出现的次数（reduce）,每一个单词需要通过键盘录入input   raw_input
"""
from functools import reduce
str = input("请输入一个字符串：")  # hello world string
# 输入方法 ['hello', 'hello', 'hello', 'apple', 'hip'];'hello', 'hello', 'hello', 'apple', 'hip';hello hello hello apple hip
list_1 = str.split(' ')  # 分给字符串，返回一个列表
print(list_1)

# 定义一个函数，用于判断该函数是否出现，+1  =1
def fun(x,y):
    if y in x:
        x[y] = x[y] + 1
    else:
        x[y] = 1
    return x

reslut = reduce(fun,list_1,{})
reslut2 = reduce(fun, ['hello', 'hello', 'hello', 'apple', 'hip'], {})  # {}为设定初始值，第一次传入的{}和第一个'hello'；第二次传入是{hello:1}和'hello'
print(reslut)
print('\n')
print(reslut2)
print('\n')



"""
第2题：用filter（）函数完成《写一段代码，输入一个年份的列表返回一个闰年的列表
闰年的判断：
   1.能被400整除的年份
   2.能被4整除，但是不能被100整除的年份
"""
def year(num):
    if num % 4 != 0 or (num % 100 == 0 and num % 400 != 0):
        return False
    else:
        return True

print(list(filter(year,range(998,2018))))

# 法2：
def years(num):
    if (num % 4 == 0 and num % 100 !=0) or (num % 400 == 0 ):
        return True
    else:
        return False

print(list(filter(years,range(998,2018))))
print('\n')



"""
第3题：请利用map函数生成0-9数字的平方组成的list。
"""
print(list(map(lambda x:x ** 2, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
print('\n')



"""
4.对以下数据进行排序（根据value值进行排序），要求使用sorted/选择/冒泡
dict = {"a":1,"b":3,"c":5,"d":6,"e":3,"f":2}
1.遍历字典中所有的value,
2.value 存放到列表中
3.sort/sorted
"""
dict = {"a": 1, "b": 3, "c": 5, "d": 6, "e": 3, "f": 2}

list1 = []
def mySort(dict):  # 遍历字典中所有的value,value 存放到列表中
    for value in dict.values():
        list1.append(value)
    return list1

list2 = mySort(dict)
print(list2)
list3 = sorted(list2)
print(list(list3))


