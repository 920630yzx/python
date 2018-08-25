# 书签管理器
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




