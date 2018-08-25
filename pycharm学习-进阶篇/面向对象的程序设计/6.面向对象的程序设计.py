class Rect:
    # 类的属性
    # 属性描述是类的对象的特性/负责存储数据
    length = 0  # 类的属性,类的对象
    width = 0   # 类的属性,类的对象

    def __init__(self, length=1, width=1):  # 类的方法，创建对象的时候，自动调用的方法。【rect = Rect()就会自动执行】用于设置对象属性的初始值
        self.width = width
        self.length = length
        print('xiaosxiao')

    def print_length_width(self):  # 方法描述的是类的对象的行为/负责管理数据
        print(self.length, self.width)  # 通过self，方法可以使用类的对象的属性，这里表示print_length_width对象也即是当前对象。

    def get_area(self):   # 获取当前矩形的面积
        return self.length * self.width

    def set_length_width(self, length, width):  # 给长和宽赋值
        self.length = length
        self.width = width


# step1 类本身只是一个类型，没有内存空间，不能储存数据。只有类的对象才能储存数据：
rect = Rect()  # 对象是一个内存空间，创建对象的时候，同时创建了length和width
rect.print_length_width()
rect = Rect(3,4)
rect.print_length_width()