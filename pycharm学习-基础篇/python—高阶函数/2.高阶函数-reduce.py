''' reduce函数:重复调用的作用
定义:
   函数会对参数序列中元素进行累积；将对一个数据集合（元祖，列表）中所有的数据都进行重复性操作：
  格式：
    reduce(funcation,iterable[,initializer])
参数说明：
   funcation:有两个参数：先对集合中第一和第二个元素进行操作，如果还有第三个，继续运算，并得到最终的结果！！！！！！
   iterable:可迭代的对象
   initializer:可选参数,可以不写----初始化参数
   返回值：返回时计算的结果 '''

# 1.案例：两个数的求和
from functools import reduce  # 使用reduce必须先导入
def add(a,b):
    return a + b
print(reduce(add,range(1,101)))  # 计算1~100之间的和
print(reduce(add, [1, 2, 3, 4, 10]))  # 直接使用add；  ans:20
print('\n')

# 2.匿名函数lambda,求和
# 方式2：
print(reduce(lambda x, y: x+y, range(1,101)))
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))









