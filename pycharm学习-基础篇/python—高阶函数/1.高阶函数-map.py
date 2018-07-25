'''1.map函数
定义：根据提供的函数对指定的序列做映射
函数语法：map(funcation, iterable)
funcation：函数    iterable：一个或者多个序列，包括列表;元祖;字符串
第一个参数funcation以参数序列中每一个元素调用funcation函数，返回包含每次funcation函数返回值的新列表
返回：
   python2    :列表
   python3   : 迭代器     列表;元祖;字符串都是可迭代的对象'''

# 1.map函数案例1
a = [1, 2, 3, 4, 5]
b = (1, 2, 3, 4, 5)
c = "xiaoming"

la = map(str, a)
print(list(la))  # ans：['1', '2', '3', '4', '5']
lb = map(str, b)
print(list(lb))  # ans：['1', '2', '3', '4', '5']
lc = map(str, c)
print(list(lc))  # ans：['x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']
print('\n')

# 2.map函数案例2
def chr2int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
list1 = ["2", "1", "6", "5"]
res = map(chr2int, list1)  # res = map(chr2int, ["2", "1", "6", "5"])也可以
print(res)
print(list(res))

# 3.map函数案例3
def chr2int(chr):
    return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]  # 以字典键值对的到结果
list1 = ["2", "1", "6", "5"]
res = map(chr2int, list1)
print(res)
print(list(res))
print('\n')

# 4.将整数元素的序列，转换为字符串型
l = map(str, [1, 2, 3, 4])  # str表示转换成字符串型，当然str是python的内置函数
print(list(l))

'''map的一些其他实例，可以看看：
def abc(a ,b, c):
    return a+b+c

list1 = [11,22,33]
list2 = [44,55,66]
list3 = [77,88,99]
ans = map(abc, list1, list2, list3)
print(ans)
print(list(ans))
print('\n')


def abc(a ):
    return a+1

list1 = (11,12,13)

ans = map(abc, list1)
print(ans)
print(tuple(ans))
print('\n')


def abc(a):
    return a+'123'

list1 = 'acbsascnboj'

ans = map(abc, list1)
print(ans)
print(list(ans))
print('\n')'''







