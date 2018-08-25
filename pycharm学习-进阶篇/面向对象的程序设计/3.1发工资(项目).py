# 1.导入另一个文件中的类，就可以在当前文件中使用另一个模块的数据
from 面向对象的程序设计.URLItemManger import URLItemManager  #第一个 URLItemManger是文件名，第二个 URLItemManger表示类名

# 创建一个manager,对其进行调用
manager = URLItemManager()
manager.add_url_item("千锋", "www.1000phone.com", 5)
manager.add_url_item("新浪网", "www.sina.com", 3)
manager.add_url_item("百度", "www.baidu.com", 4)

manager.delete_url_item_url("www.baidu.com")
manager.print_content()



# 2.继承可以用来统一接口
class ReciveMoney:
    def recive_money(self, money):
        return


class Worker(ReciveMoney):
    totalMoney = 1000

    def recive_money(self, money):
        self.totalMoney += money


reciver = Worker()
reciver.recive_money(800)
print(reciver.totalMoney)  # 1800

# # 收钱父类，写出来，只是规范，用什么方法来接受钱
# class ReciveMoney:
#     def recive_money(self, money):
#         return


# 老板
class Boss:
    # 这个属性暂时随便做了各初始化，实际上这个属性将会用收钱的对象进行赋值
    #reciver = ReciveMoney()

    # 发钱
    def send_money(self, money):
        # 我不知道谁会收钱，但是我知道它就是ReciveMoney的子类，他拥有收钱的方法
        self.reciver.recive_money(money) # 注意reciver = Worker()
        return


class Worker(ReciveMoney):
    total_money = 1000

    def recive_money(self, money):
        self.total_money += money

    def show_money(self):
        print("I have ￥", self.total_money)


mr_zhang = Boss()
lao_wang = Worker()
# 首先建立代理关系
mr_zhang.reciver = lao_wang
lao_wang.show_money()
mr_zhang.send_money(10000)
# self.reciver.recive_money(money)
lao_wang.show_money()





