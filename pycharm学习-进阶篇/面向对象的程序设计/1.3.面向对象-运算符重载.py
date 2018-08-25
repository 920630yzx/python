# 1.运算符重载
class Rect:
    length, width = 0, 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):  # __add__表示加法
        new_rect = Rect(self.length + other.length, self.width + other.width)  #注意！！！__add__()方法表示相加， Rect为重载
        return new_rect  #返回new_rect

    def __sub__(self, other):  # __add__表示减法
        return 0

    def __mul__(self, other):  # __add__表示乘法
        return 0

    def __divmod__(self, other):  # __add__表示除法
        return 0

    def __mod__(self, other):   #取余数
        return 0

    def __pow__(self, power):   #乘方
        return 0

    # 描述函数，返回值是一个字符串，当打印当前类的对象，就是打印这个函数的返回值
    def __str__(self):
        return "hello world !!!"


rect1 = Rect(1, 2)
rect2 = Rect(4, 5)
rect = rect1 + rect2 + rect2
# rect1 + rect2 相当于 rect1.__add__(rect2).__add__(rect2)
print(rect.get_area())

utl=Rect(3,5)
print(utl)



# 私有属性
print('\n')
class Man:
    # 定义类变量 __ 两个下划线代表私有属性
    __age = 18
    __sex = '男'
    def getAge(self):
        print(self.__age)
        return self.__age


    def getName(self):
        print(self.__sex)
        return self.__sex

# 由于是私有属性，就不能在类外直接调用了，故而没有m.__age，只有通过m.getAge()来间接的调用。当然私有属性也不能被继承
m = Man()
m.getAge()
m.getName()
