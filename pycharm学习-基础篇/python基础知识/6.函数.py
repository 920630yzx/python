# 函数
# 有一些工作可能是反复需要被使用的
# 开发成本浪费效率（复制粘贴），增加维护成本
# 可以将那些反复使用的简单功能，封装成函数，方便反复使用

# 最简单的函数，没有参数，没有返回值

# 封装一个打印5个hello world的函数
# C C++ Python 小写字母+下划线分割单词 print_hello_world
# Java C# Objective-C swift spark 驼峰法 printHelloWorld
# QF_printHelloWorld

def printHellowords( ):
    # 在函数体当中可以编写和函数体外一样的任意代码
    for i in range(0, 3):
        print("Hello, world!!!")

# 调用函数
printHellowords()

# 1.定义函数
def hello():
    print("hello, world!")
    # 【函数】中的代码就和函数外没有区别，函数外怎么写，里面就怎么写

print("Do sth!")
hello()

# 为了能够更好的封装功能，需要和函数体外面的数据进行交互，因此通过参数将函数体外的数据传入函数中
# 2.封装函数，打印两个数字的立方和
def sum_x(num1, num2):    # num1 和num2 称为sumX的【形参】
    # 形参是变量
    # 实参是值
    # 调用函数时发生传参
    # 传参就是用实参给形参赋值 相当于 num1, num2 = 3, 2
    print(num1 ** 3 + num2 ** 3)

sum_x(3, 2)  # 3 和 2 就是sumX的【实参】

# 求体积
def volume_of_cube(length, width, height):
    print(length * width * height)

volume_of_cube(1, 2, 3)
volume_of_cube(2, 1, 2)
print('\n')


# 【注】在Python传参当中需要考虑所传递的参数是【函数内可变参数】还是【函数内不可变参数】
# 在Python当中基础数据类型和Str tuples(元组) 都是在函数内不可变的，list和dict是函数内可变的 ！！！
# 3.有一个用于修改数据的函数
def change_data(data):  # data = a   data = 5
    data = 5

a = 6
change_data(a)
print(a)

# step2:list和dict是函数内可变的!!!
def change_list(list1):  # list1 = listX
    list1[0] = 5
    list1[1] = 6

listX = [1, 2, 3, 4, 5]
change_list(listX)
print(listX)

# step3:  ！！！
list2 = listX       # list2 和listX确实是不同的内存空间 跟b和a没有区别
                    # 列表是一个数据结构，记录了元素数据在内存中的位置
                    # list2 和 listX 值相等，意味着存储了同样的内存寻址
                    # list2[0]其实是寻址过程

list2[0] = -1
list2[1] = -9
print(list2)
print(listX)  # 为何修改list2会改变listX？


# 4.参数默认值/缺省值，声明函数的时候可以设置形参的默认值
def sum_nums(u=4, v=1, w=5):
    print(u + v + w)

sum_nums()

# 传参时可以指定传参的形参
sum_nums(v=2, w=3, u=1)
sum_nums(v=9)


# 5.不定长参数，有的时候参数个数不定
# 求n个数的平方和
def sum_y(*nums):  # *nums表示不定长参数
    s = 0
    for i in nums:
        s += i ** 2
    print(s)

sum_y(1, 2, 3, 4)


# 6.函数的形参可以同时有定长的和不定长的两种，将不定长部分写在最后
def sum_yy(do_it, *nums):
    if do_it:
        s = 0
        for i in nums:
            s += i ** 2
        print(s)


sum_yy(True, 1, 2, 3, 4, 5)
sum_yy(1, 1, 2, 3, 4, 5)

# 7.返回值
def sum_nums(a1, b1):
    # print(a1 + b1)
    return a1 + b1      # 跟在return关键字后面的表达式的值就是返回值,返回值就是函数调用表达式的值


ret = sum_nums(1, 2)    # 返回值就是函数调用表达式的值
print(ret)
print(sum_nums(1, 1) * 2)

# 另外，作为不需要返回值的函数，return后面可以什么都没有，表示函数到此结束
def larger_than_5(numX):
    if numX > 5:
        print("大于")
        return  # return会自动终止函数,break是自动终止循环的函数
    print("不大于")

larger_than_5(6)


# 8.作用域：全局变量与局部变量
num=7
def num_change():
    num=6   # 如果在函数体内申明变量,可以和函数体外的变量同名,但是是一个全新的变量,作用域是从声明到函数结束
    print('函数体内:',num)

num_change() #运行函数
print('函数体外:',num)
print('\n')


# 9.全局变量 global
a,b = 1,2
def get_num():
    global a,b
    a=11
    b=12
    print(a, b)
print(a,b)    # 1 2
get_num()    # 11 12
print(a,b)  # 11 12

# step2：nonlocal
def func1():
    num=10
    def func2():
        num=9
        print('func2', num)
    func2()  # 表示在函数中调用func2
    print('func1', num)

func1()  # 可以得到两个不同结果，func2 9,func1 10说明有两个num只是名称不同

# step3：nonlocal
def func1():
    num = 10
    def func2():
        nonlocal num   # 通过关键字引用到函数体外的局部变量
        num = 9
        print('func2', num)
    func2()  # 表示在函数中调用func2
    print('func1', num)

func1() # 可以得到相同的结果，都等于9