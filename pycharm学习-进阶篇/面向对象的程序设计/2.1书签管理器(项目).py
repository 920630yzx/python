# 书签管理器
# 编写一个书签管理器即收藏夹模块，负责管理浏览器中的收藏夹，其功能为储存并管理书签
#
# 1.每个书签包括如下信息:
# 标题
# 网址
# 星级
# 访问次数

# 2.收藏夹具备功能有:
# 添加书签（标题不可重复）
# 删除书签（通过标题或网址查找）
# 根据标题查找书签信息
# 修改书签的标题（通过标题查找）
# 修改书签的网址
# 修改书签的星级
# 归零书签的访问次数
# 打印书签标题列表
# 打印书签详情列表

# 3.需求当中有两个类  收藏夹、书签
# 从功能看，应该先写书签

# 书签类，其对象为一个书签，负责存储一个网址的相关信息
class URLItem:
    title = ""  # 标题
    URL = ""    # 网址
    stars = 0   # 星级
    visits = 0  # 访问次数

    def __init__(self, title, url, stars):
        self.title = title
        self.URL = url
        self.stars = stars

    # 访问次数增加的方法
    def visits_up(self):
        self.visits += 1


# 收藏夹类，其对象负责管理大量的书签对象
class URLItemManager:
    # 通过列表存储大量的书签
    __urlItemList__ = [] # 私有属性

# 添加书签（标题不可重复）低耦合
    def add_urlitem(self, title, url, stars):

        # 判断书签标题是否重复
        # for item in self.urlItemList:
        #     if item.title == title:
        #         print("添加书签失败，标题", title, "重复")
        #         return
        item = self.find_urlitem(title)  # find_urlitem定义在下面
        # None False 0 是假
        if item != None:
            print("添加书签失败，标题", title, "已经存在")
            return

        # 创建一个书签
        url_item = URLItem(title, url, stars)  # URLItem？
        # 把书签存到当前收藏夹中
        self.__urlItemList__.append(url_item)
        print("书签", title, "创建成功")

# 删除书签（通过标题或网址查找）
    def delete_urlitem_title(self, title):
        item = self.find_urlitem(title)
        if item == None:  # 或者 if not item:
            print("删除失败，书签", title, "不存在")
            return

        # 如果存在标题为title的书签，那就是item
        self.__urlItemList__.remove(item)
        print("书签", title, "删除成功")

# 通过网址删除书签（作业）？自己写的，还未检验
    def delete_url_item_url(self, url):
        count = 0   # 与上面不同之处在于是使用了循环，而不是调用类中自定义的函数
        for item in self.__urlItemList__:
            if item.url == url:
                self.__urlItemList__.remove(item)
                count += 1
        if count > 0:
            print("删除网址为", url, "的书签", count, "条")
        else:
            print("删除书签失败，没有该网址的书签")



# 根据标题查找书签信息
    def find_urlitem(self, title): # 如果item在__urlItemList__中，则返回这个item；否则返回None
        for item in self.__urlItemList__:
            if item.title == title:
                return item
        # 在Python当中，查找对象，如果没有找到，返回一个None，表示不存在
        return None

# 修改书签的标题（通过标题查找）
    def change_urlitem_title(self, old_title, new_title):
        # 首先找到需要修改标题的书签
        item = self.find_urlitem(old_title)
        if item == None:
            print("修改失败，书签", old_title, "不存在")
            return
        item.title = new_title
        print("书签", old_title, "标题已修改为", new_title)

# 修改书签的网址(作业)
# 修改书签的星级(作业)
# 归零书签的访问次数(作业)
# 打印书签标题列表
    def show_items_title(self):
        print("=============================")
        for item in self.__urlItemList__:
            print(item.title)
        print("=============================")

# 打印书签详情列表
    def show_items_content(self):
        print("=============================")
        for item in self.__urlItemList__:
            print("标题：", item.title)
            print("网址：", item.URL)
            print("星级", item.stars)
            print("访问次数", item.visits)
            print("")
        print("=============================")

# def add(a, b):
#     return a + b

# manager是对象的引用
manager = URLItemManager()
manager.add_urlitem("千锋", "www.1000phone.com", 5)
manager.add_urlitem("百度", "www.baidu.com", 5)
manager.add_urlitem("千锋", "www.1000phone.com", 5) # 添加书签失败，标题 千锋 已经存在
manager.show_items_title() # 得到答案：千锋   百度
manager.delete_urlitem_title("百度")
manager.show_items_title() # 得到答案：千锋
manager.delete_urlitem_title("百度") # 删除失败，书签 百度 不存在
manager.add_urlitem("新浪", "www.sina.com", 4) # 书签 新浪 创建成功
manager.show_items_content() # 这里是打印书签详情列表

# manager.__urlItemList__.append(5)





