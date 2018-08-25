# 通过队列管理线程
import threading
import queue
import time


# 写一个类，继承自线程类
class MyThread(threading.Thread):

    def __init__(self, word):
        super().__init__()
        self.word = word

    def run(self):  # run重写，run也是threading.Thread的一个方法
        q.put(self.word)  # q = queue.Queue(5)说明只有5个可以put进去，直到q.get()输出队列才能继续q.put(self.word)输入，因此会造成阻塞
        self.print_hello_world(2)
        q.get()  # 执行完q.put(self.word)和self.print_hello_world(2)后才能执行这一步q.get()
        return

    def print_hello_world(self, delay):
        for i in range(0, 10):
            # print(word)
            time.sleep(delay)
            print("hello world!", self.word)


# 通过全局队列管理线程
q = queue.Queue(5)

thread_words = ["第一", "第二", "第三", "第四", "第五", "第六", "第七", "第八"]
for word in thread_words:
    thread = MyThread(word)  # 调用def __init__(self, word):
    thread.start()  # 调用def run(self):函数

while True:
    pass
