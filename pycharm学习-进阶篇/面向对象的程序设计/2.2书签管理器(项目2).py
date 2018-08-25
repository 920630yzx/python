# 书签管理器 (这里与前面一章类似，做个补充)
# 编写一个书签管理器即收藏夹模块，负责管理浏览器中的收藏夹
# 其功能为储存并管理书签
#
# 每个书签包括如下信息
# 标题
# 网址
# 星级
# 访问次数
#
# 收藏夹具备功能有
# 添加书签（标题不可重复）
# 删除书签（通过标题或网址查找）
# 根据标题查找书签信息
# 修改书签的标题（通过标题查找）
# 修改书签的网址
# 修改书签的星级
# 归零书签的访问次数
# 打印书签标题列表
# 打印书签详情列表


# 书签类，其对象储存单独一个书签的信息
class URLItem:
    title = ""
    url = ""
    stars = 0
    visits = 0

    def __init__(self, title, url, stars):
        self.title = title
        self.url = url
        self.stars = stars

    # 描述函数，返回值是一个字符串，当打印当前类的对象，就是打印这个函数的返回值
    def __str__(self):
        return "标题：{}\n网址：{}\n星级：{}\n访问次数：{}".format(self.title,
                                                    self.url, self.stars,
                                                    self.visits)   # .format,这里是字符串的拼接替换方式

utl_item = URLItem('百度','www.baidu.com',5)
print(utl_item)

# 书签管理类，其对象是一个收藏夹，储存并管理大量的书签对象
class URLItemManager:
    __url_items = []

    # 添加书签（标题不可重复）
    def add_url_item(self, title, url, stars):
        # 首先判断新书签的标题是否和已有标签冲突
        item = self.find_url_item(title)
        if item != None:
            print("添加书签", title, "失败，标题已存在")
            return

        new_item = URLItem(title, url, stars)
        self.__url_items.append(new_item)
        print("书签", title, "添加成功")

    # 删除书签（通过标题或网址查找）
    def delete_url_item_title(self, title):
        item = self.find_url_item(title)
        if item == None:
            print("删除书签", title, "失败，书签不存在")
            return
        # 如果存在标题为title的书签，就是item
        self.__url_items.remove(item)
        print("书签", title, "删除成功")

    def delete_url_item_url(self, url):
        count = 0
        for item in self.__url_items:
            if item.url == url:
                self.__url_items.remove(item)
                count += 1
        if count > 0:
            print("删除网址为", url, "的书签", count, "条")
        else:
            print("删除书签失败，没有该网址的书签")

    # 根据标题查找书签信息
    def find_url_item(self, title):
        for item in self.__url_items:
            if item.title == title:
                return item
        return None

    # 修改书签的标题（通过标题查找）
    def change_url_item_title(self, old_title, new_title):
        item = self.find_url_item(old_title)
        if item == None:
            print("没有标题为", old_title, "的书签")
            return
        item.title = new_title
        print("已修改书签", old_title, "标题为", new_title)

    # 修改书签的网址
    # 修改书签的星级
    # 归零书签的访问次数
    # 打印书签标题列表
    def print_titles(self):
        print("===========================")
        for item in self.__url_items:
            print(item.title)
        print("===========================")

    # 打印书签详情列表
    def print_content(self):
        print("===========================")
        for item in self.__url_items:
            print(item, "\n")
        print("===========================")






'''补充'''
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






