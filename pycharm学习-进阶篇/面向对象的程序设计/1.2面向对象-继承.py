'''
5.面向对象编程的特点
1.继承性,是指编程中父子集之间关系的描述
【注】：继承和派生是对类之间继承关系的两种描述；当子类继承父类，会获得父类的属性和方法，也会派生自己的属性和方法。
2.多态,是指同样的函数名，可以有不同的函数体，实现不同的功能，称为多态。
3.重写，如果子类继承父类的方法，但是子类认为这个方法不适合子类使用，可以重新写一个同名的方法，同名方法自动覆盖父类的方法
'''

'''【多继承】在Python语言中，一个子类可以继承多个父类，同时会获得多个父类的属性和方法，称为【多继承】
【多继承实现代理委托】【代理】是一种【设计模式】，即【代理】是一种非常常用的编程思想，目的是实现对象间的数据传递
子类可以继承两个父类，两个父类的顺序非常重要；当两个父类拥有同名的方法时，子类会优先使用前面的父类的方法。'''

# 1.继承：单继承
class Parent:
    a, b, c = 0, 0, 0

    def set(self, a, b, c):  #给a,b,c分别赋值
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(self.a, self.b, self.c)


# 创建一个子类，继承自Parent
class Child(Parent):
    d = 0

Child=Child()
Child.a=1
Child.d=3
Child.show()
Child.set(1,2,3)
Child.show()
print('\n')


# 2.继承：单继承  (与上例类似)
class Parent:
    a, b, c = 0, 0, 0

    def set(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        print(self.a, self.b, self.c)


# 创建一个子类，继承自Parent
class Child(Parent):
    d = 0

    def set(self, a, b, c, d): # 这里就是重写
        # 通过super()函数可以调用父类已经被覆盖的同名方法!!!
        super().set(a, b, c)
        self.d = d

    def show(self):   # 这里也是重写
        print(self.a, self.b, self.c, self.d)


child = Child()
child.show()
child.a = 9
child.d = 10
child.show()
child.set(1, 2, 3, 4)
child.show()
print('\n')


# 3.继承是可以传递的：
class GrandChild(Child):
    e = 0

    def print_hw(self):
        print("hello world!", self.e)


grandChild = GrandChild()
grandChild.a = 10
grandChild.b = 11
grandChild.c = 12
grandChild.d = 13
grandChild.e = 10

grandChild.show()
grandChild.print_hw()



# 4.多继承：也就是同时继承两个父类，两个父类的顺序非常重要
class Father:
    name = ""

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("I am father, I am", self.name)

    @staticmethod  # 静态变量，直接打印输出
    def show():
        print("I am father!")


class Mother:
    age = 0

    def __init__(self, age):
        self.age = age

    def show_age(self):
        print("I am mother, I am", self.age)

    @staticmethod
    def show():
        print("I am mother")


# 子类可以继承两个父类，两个父类的顺序非常重要；当两个父类拥有同名的方法时，子类会优先使用前面的父类的方法。
class Son(Father, Mother):
    level = 0

    def __init__(self, name, age, level):
        # 调用父类构造方法，需要传参self !!!
        Father.__init__(self, name)
        Mother.__init__(self, age)
        self.level = level  # 子类独有

    @staticmethod  # 静态变量，直接打印输出
    def show():
        Mother.show()  # 输出Mother.show的静态变量


son = Son("张晓峰", 12, 70)
son.name = "伊利丹"  # 这里会将Son.name重置
son.age = 3500

son.show_name() # 答案：I am father, I am 伊利丹
son.show_age() # 答案：I am mother, I am 3500

son.show()


# 5.构造方法的重写
class Parent:
    a, b = 0, 0

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Child(Parent):
    c = 0

    def __init__(self, a, b, c):
        Parent.__init__(a, b)
        self.c = c





'''补充：
# 私有属性
class Parent:
    # 公有属性
    name = ""
    # 私有属性, 前面加两个下滑线，就会变成私有属性:私有属性不能在类外或子类当中直接调用，必须通过当前类的对象和方法进行使用
    __name = ""
    # 保护属性, 前面加一个下划线，就会变成保护属性:保护属性只能在当前对象或者子类对象中使用，不能在类外使用
    _name = ""

    # 私有属性不能在类外或子类当中直接调用，必须通过当前类的对象和方法进行使用
    # 保护属性只能在当前对象或者子类对象中使用，不能在类外使用
    # 官方的私有方法，会前后各加两个下划线，防止和自定义方法命名冲突：
    # 私有方法与私有属性类似，不能在类外或子类当中直接调用，必须通过当前类的其他方法进行调用
    # 保护方法与保护属性类似，只能在当前对象或者子类对象中使用，不能在类外使用
    #【类方法】类方法可以使用对象的属性，调用类方法使用类名，类方法可以用于改变对象中的引用属性的初始对象数据
    def set_name(self, name):
        self.__name = name

    def get_name(self, name):
        self.__do_it__()
        return self.__name

    def __do_it__(self):  # 定义私有方法，私有方法与私有属性类似，不能在类外或子类当中直接调用，必须通过当前类的其他方法进行调用
        print("do it!!", self.name)

    # 如果一个方法即没有使用对象的属性，也没有使用类当中其他对象的方法，那么就要声明为静态方法:
    # 静态方法，可以用对象调用，也可以用类名调用
    @staticmethod   # 申明为静态方法
    def do_it_again():
        print("hello, world!")


class Child(Parent):
    def do_sth(self):
        # self.__name = "55" # 不要这样干,因为__name是私有属性
        self.set_name("55")  # 通过父类的方法可以调用父类的属性
        self._name = "!!"


laoba = Parent()
laoba.name = "张老三"
laoba.__name = "刘老六"
laoba._name = 'adf'
print(laoba.__name)
print(laoba._name)

laoba.do_it_again()
Parent.do_it_again()  # 直接调用

# laoba._name = "123"
# laoba.__init__()
# print(laoba.__name__)
'''







