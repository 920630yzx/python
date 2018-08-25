# 线程锁

import threading
import time


class Mythread(threading.Thread):

    def __init__(self, word):
        super().__init__()  # 通过super()函数可以调用父类已经被覆盖的同名方法!!!
        self.word = word

    def print_helloworld(self):
        for i in range(0, 20):
            time.sleep(1)
            print("hello world", self.word, i)

    # 这里就是原子操作
    def run(self):  # run重写，run也是threading.Thread的一个方法
        # 加锁
        threadLock.acquire()
        self.print_helloworld()
        # 解锁
        threadLock.release()


# 创建一个线程锁，线程锁创建在类的外面，唯一一把
threadLock = threading.Lock()


thread1 = Mythread("第一")
thread2 = Mythread("第二")
thread1.start()
thread2.start()

while True:
    pass

