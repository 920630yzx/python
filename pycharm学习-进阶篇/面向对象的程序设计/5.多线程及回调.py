# 回调
# 在实际工作当中，一个对象如果想实现某个功能，但自身不具备相关方法，可以借用拥有该方法的功能模块，即借用其他对象完成某个功能
# 当指派某个对象A，完成某个耗时功能，一般为了防止主线程阻塞。会将耗时功能放到子线程中完成，主线程继续完成其他任务，当耗时功能完毕，
# 被指派的对象A完成任务，需要通过回调，通知主线程，并回传(通过回调函数)处理完毕的数据

# 耗时操作有很多，下载，存储，压缩，解压，编码，解码，转码
# 这里举一个耗时下载的例子
# 多线程，两个线程可以在同一时间做不同的事情，采用时分复用

# # 1.导入线程模块
# import threading
# import time
#
# # 为了回传数据，通过继承，在父类当中规范接收数据的方法
# class ReciveData:
#     def recive_data(self, data):
#         return
#
#
# # 模拟一个用于下载的专用模块
# class Download:
#     delegate = ReciveData() # delegate是ReciveData()的一个类型
#
#     # 继承线程类，线程类当中写在run函数中的方法会跑在单独县城里
#     # 重写这个方法
#     def run(self):
#         self.download()
#
#     def download(self):
#         for i in range(0, 10):
#             time.sleep(1)  # 线程停止工作1秒钟，休眠1秒
#             print('hello world')
#         data = "我就是10秒下载的数据"
#         self.delegate.recive_data(data)  # 下载数据后，我要回传数据
#
# K = Download()
# K.download()



# 2.修改下
# 导入线程模块
import threading
import time

# 为了回传数据，通过继承，在父类当中规范接收数据的方法
class ReciveData:
    def recive_data(self, data):
        return


# 模拟一个用于下载的专用模块
class Download(threading.Thread):  # 继承自threading模块下的Thread类
    delegate = ReciveData()

    # 继承线程类，线程类当中写在run函数中的方法会跑在单独线程里
    # 重写这个方法
    def run(self):
        self.download()

    def download(self):
        for i in range(0, 10):
            # 线程停止工作1秒钟，休眠1秒
            time.sleep(1)
            print('hello world!!!')
        data = "我就是100秒下载的数据"
        # 下载数据后，我要回传数据
        self.delegate.recive_data(data)

download=Download()
download.start()  # start()继承自父类threading.Thread,表示开启线程（子线程）

while 1:           # 这里是主线程
    print('bitch')
    time.sleep(2)



''' 回调函数就是一个通过函数指针调用的函数。如果你把函数的指针（地址）作为参数传递给另一个函数，
    当这个指针被用来调用其所指向的函数时，我们就说这是回调函数。 '''

