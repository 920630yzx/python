'''
filter函数  过滤作用
定义：该函数用于过滤序列，过滤掉不符合条件的元素
返回值：由符合条件元素组成的新的列表
格式：filter(funcation, iterable)
参数说明：
funcation: 函数，接受两个参数，（判断）
iterable: 序列（可迭代的对象），序列的每一个元素作为参数传递给函数，进行判断（true, false）
返回值：将返回的True所对应的数据存放到一个新的列表
功能：过滤序列 '''

# 1.案例：筛选指定的元素
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def func(num):
    if num % 2 == 0:  # 偶数保留
        return True  # 偶数保留
    return False   # 奇数删除

k= filter(func,list1)
print(k)
print(list(k))  # ans:[2, 4, 6, 8]
print(tuple(k))  #  ans:(),这里比较特殊
print('\n')


# 2.案例:
list2 = [['姓名', "年龄", "爱好"], ["tom", 25, "无"], ["hanmeimei", 26, "pashan"]]

def fun2(v):
    v = str(v)
    if v == "无":
        return False
    else:
        return True

# step1:
for line in list2:
    print(line)
print('\n')

# step2:
for line in list2:
    v = str(line)
    print(v)
print('\n')

# step3: 可以发现'无'字没有了
for line in list2:
    m = filter(fun2, line)
    print(list(m))

"""
number  int  flaot  bool  comple
string  '' ""
list    []   可变
tuple  ()    不可变
dict   {}    可变
set    (集合)


可变类型
不可变类型

序列（容器）
"""






















