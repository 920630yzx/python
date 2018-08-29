# 1.排列
'''
排列的定义：
    从n个不同的元素中取出m个元素（m<=n）,按照一定的顺序排成一列，
    m == n 全排列
list = [1,2,3,4,5,6,7,8,9]
涉及一个模块：itertools
# 关键函数：itertools.permutations(参数1，参数2)  参数1：迭代对象:String,list,dict;  参数2：m;
'''
import itertools
myList = list(itertools.permutations([1, 2, 3, 4], 1))  # 得到4种可能
print('第一种可能:', myList)
print(len(myList))
print('\n')

myList1 = list(itertools.permutations([1, 2, 3, 4], 2))  # 得到4*3=12种可能
print('第二种可能:', myList1)
print(len(myList1))
print('\n')

myList2 = list(itertools.permutations([1, 2, 3, 4], 3))  # 得到4*3*2=24种可能
print('第三种可能:', myList2)
print(len(myList2))
print('\n')



# 2.组合
'''
从m个不同额元素中，任意取出n元素为一组（n <= m）  
涉及一个模块：itertools
关键函数：itertools.combinations '''

import itertools
myList = list(itertools.combinations([1, 2, 3, 4, 5], 3))  # 相当于C5(3)
print(myList)
print(len(myList))
print('\n')

myList1 = list(itertools.combinations([1, 2, 3, 4, 5], 4))  # 相当于C5(4)
print(myList1)
print(len(myList1))
print('\n')



# 3.案例   密码破解：
'''破解一个数字和字母组成的六位数密码;    数字:0~9   字母:a~z  A~Z;      随机生成一个6位数的密码'''

import itertools
mylist = list(itertools.product("0123456789", repeat=2))  # 密码为2位，全部从"0123456789"进行选择;如果没有list则返回的是储存空间的位置
passwd = list(("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyyuioasdfghjklzxcvbnm", repeat=2)))  # "0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyyuioasdfghjklzxcvbnm"表示类型，与前者类似
passwd2 = ("".join(x) for x in itertools.product("0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyyuioasdfghjklzxcvbnm", repeat=2))

while True:
    try:
        str = next(passwd2)   # next表示不断向后调用passwd2（非列表）,一次一次的调用,直到结束
        print(str)
    except StopIteration as a:   # 有异常则跳出循环，StopIteration表示停止异常
        break

# print('所有密码的可能:', mylist)
# print(len(mylist))
#
# print('所有密码的可能:', passwd)
# print(len(passwd))


