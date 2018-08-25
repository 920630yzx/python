'''一、面向对象初认识
【面向过程】面向过程的编程，关注点在数据的处理，就像小学解应用题，处理数据，运算数据是核心，体现是数学逻辑
【面向对象】面向对象的编程，关注点在程序中的对象，将生活逻辑带入到编程当中

二、类和对象
1.从生活逻辑上理解
人类		你、我、诸葛亮、曹操、贞德、蔡英文
超级英雄	钢铁侠、超人、美国队长
变形金刚	擎天柱、威震天
超级赛亚人	卡卡罗特、贝吉塔、特兰克斯

2.代码上理解
【类】是一个自定义的类型
【对象】是该类型创建的变量

3.从数据管理的角度理解
【属性】存储数据
【方法】管理数据

4.官方定义
【类】是具有相同特性的对象的抽象
【对象】是类的具体表现形式

5.面向对象编程的特点
1.继承性,是指编程中父子集之间关系的描述
【注】：继承和派生是对类之间继承关系的两种描述；当子类继承父类，会获得父类的属性和方法，也会派生自己的属性和方法。
2.多态,是指同样的函数名，可以有不同的函数体，实现不同的功能，称为多态。
3.重写，如果子类继承父类的方法，但是子类认为这个方法不适合子类使用，可以重新写一个同名的方法，同名方法自动覆盖父类的方法
 '''


# 1.定义一个类
class Rect:
    # 类的属性
    # 属性描述是类的对象的特性/负责存储数据
    length = 0  # 类的属性,类的对象
    width = 0   # 类的属性,类的对象

    def __init__(self, length=1, width=1):  # 类的方法，一旦类被调用就会自动执行，用于设置对象属性的初始值
        self.width = width
        self.length = length
        print('xiaoxiao')

    def print_length_width(self):  # 方法描述的是类的对象的行为/负责管理数据
        print(self.length, self.width)  # 通过self，方法可以使用类的对象的属性，这里表示print_length_width对象也即是当前对象。

    def get_area(self):   # 获取当前矩形的面积
        return self.length * self.width

    def set_length_width(self, length, width):  # 给长和宽赋值
        self.length = length
        self.width = width


# step1 类本身只是一个类型，没有内存空间，不能储存数据。只有类的对象才能储存数据：
rect = Rect()   # 对象是一个内存空间，创建对象的时候，同时创建了length和width
rect.print_length_width()  # 直接输出  结果： 1  1   ‘def __init__(self, length=1, width=1): 创建对象的时候，自动调用的方法，用于设置对象属性的初始值’
# step2 使用对象的属性，赋值：
rect.length = 9
rect.width = 10
# step3 调用对象的方法：
rect.print_length_width()  # 结果： 9  10
# step3 调用对象的方法:
rect = Rect(3, 4)  # 结果：xiaoxiao
rect.print_length_width()
print('\n')

'''三、直面面向对象程序
【例】小明手里有两张牌，左手红桃A，右手黑桃K，现在小明交换两手的牌，问，交换后，两手中各是什么牌？
三个 五个
小明 两张牌
小明 两只手 两张牌'''
# 2.一个类可以创建多个对象，多个对象是不同的变量，不同的内存空间，互不影响
rect1 = Rect()
rect1.length = 2        # 给类的对象赋值
rect1.width = 3         # 给类的对象赋值

rect1.print_length_width()  # 结果： 2 3
rect.print_length_width()   # 结果： 9 10

rect1.set_length_width(3, 4)  # 更改属性/对象，重新赋值
rect1.print_length_width()   # 结果： 3 4

# 创建对象的时候，即可调用构造方法初始化
print('rect1面积',rect1.get_area())
rect2 = Rect(5, 6)
print("rect2面积", rect2.get_area())
print('\n')


# 2.小明交换牌例题

# 写出牌的类
class Poker_card:
    color = ""
    num = ""

    def __init__(self, color, num):
        self.color = color
        self.num = num

    def set_color_num(self, color, num):
        self.color = color
        self.num = num

# 写出手的类
class Hand:
    card = Poker_card("", "")

# 写出人的类
class Human:
    # 人有两只手
    left_hand = Hand()
    right_hand = Hand()

    # 人有哪些行为
    # 持牌
    def catch_cards(self, card1, card2):
        self.left_hand.card = card1
        self.right_hand.card = card2

    # 交换牌
    def swap_cards(self):
        tmp_card = self.left_hand.card
        self.left_hand.card = self.right_hand.card
        self.right_hand.card = tmp_card

     # 展示牌
    def show_cards(self):
        print("=============================================")
        print("左手牌", self.left_hand.card.color, self.left_hand.card.num)   # 注意这个的联系 self.left_hand.card.color 类似于不断的继承
        print("右手牌", self.right_hand.card.color, self.right_hand.card.num)
        print("=============================================")

xiaoming = Human()
cardA = Poker_card("红桃", "A")
cardB = Poker_card("黑桃", "K")

xiaoming.catch_cards(cardA, cardB)  # 这里比较难理解
xiaoming.show_cards()
xiaoming.swap_cards()
xiaoming.show_cards()












