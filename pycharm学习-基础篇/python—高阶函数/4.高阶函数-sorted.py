''' sorted函数：   排序作用
定义：
sorted函数对所有的可以迭代的对象进行排序

sort和sorted区别？
sort只用于列表排序
sorted: 对所有的可以迭代的对象进行排序,返回值是一个重新排列的列表, 而不是在原来的继基础上进行操作

格式：
sorted(iterable[, cmp[], key[, reverse]])  !!!
参数的说明：
iterable：可迭代的对象

cmp: 比较函数，具有两个参数，参数的值都是从可迭代的对象中取出，(可省略)
该函数必须遵守
大于 返回1
小于 返回- 1
等于 返回0

key: 用来比较的参数，只有一个参数  (可省略)

reverse：排序的规则，reverse = True 表示降序；false(默认)是升序'''

list = [1, 2, 3, 2, 1, 3, 5, 2, 3, 1]
list1 = sorted(list, reverse=True)  # reverse = True 表示降序
print(list1)
print('\n')


list = [1, 2, -3, 2, -1, 3, 5, -2, 3, 1]
list1 = sorted(list,key=abs)  # 按照绝对值的方式进行排序
print(list)
print(list1)

list1 = sorted(list, key=abs, reverse=True)  # 按照绝对值的方式进行排序
print(list1)
print('\n')


# 2.自己定义一个函数
def myLen(str):
    return len(str)

list2 = ["a1111","b222222","c33333333","d44"]

list3 = sorted(list2, key=myLen)
print(list3)
list3 = sorted(list2, key=myLen, reverse=True)
print(list3)

