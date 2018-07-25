#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(10000)  # 这句话可以修改递归迭代次数

# 1递归: 函数调用其他函数,或者函数调用本身。注意: 所有的递归都能用for循环来实现。递归主要解决的是深层次遍历问题,如果不知道有多少层,特别适合用递归.
# 注意递归每执行一次就会在栈里面创建一个栈针,但是在python 里面递归的最大次数是1000 次
# 1.1例题：5以内相乘 n阶乘  5 * 4 * 3 * 2 * 1,先用常规方法求解：

result = 1
for index in range(1,6):  # 使用for循环，for循环包左不包右的
    result *= index  # result = result * index

print(result)


# 1.2用递归解决上面的问题：
def ji(n):
    if n == 1:
       return 1
    else:
        return n * ji(n-1)

print (ji(5))

# 递归在栈里面的运行方式
# 递归在栈里面存的是表达式 5! = 5 * ji(4)
# 4! = 4 * ji(3)
# 3! = 3 * ji(2)
# 2! = 2 * ji(1)
# 1! = 1


# 1.3定义一个函数,求1到100的和
def sumss(n):
    if n == 1:
        return 1
    else:
        return n + sumss(n-1)

print (sumss(100))  # 求1到100的和，如果计算1到1001和话就会崩溃【sumss(1001)】，因为递归不能超过1000次
print (sumss(1001))


# 1.4斐波那契数列
# 0 1 1 2 3 5 8 13 21

def current(n):
    if n == 0:
        return n
    if n == 1:
        return n
    return current(n-1) + current(n-2)

print(current(8))

# 为什么不用for循环而使用递归
# for 循环同样的内容比递归做同样的内容使用的时间短；原因就是for循环只有一个变量不停的进行结算,而递归在栈里面存的是表达式,最后进行计算
# 使用递归的场景就是层次不可预测,比如遍历文件夹,不知道有多少层,那我们就使用递归


# 2.for循环与递归
# 2.1for循环所用时间 计算1*2*3*...1000
from time import clock

result = 1
clock()
for index in range(1, 1000):
    result *= index

print('for循环所用的时间是：',clock())


# 2.2递归所用时间  计算1*2*3*...1000
def jin(n):
    if n == 1:
        return n
    else:
        return n *ji(n-1)

# 调用递归
clock()
jin(1000)
print('递归所用的时间是：',clock())

