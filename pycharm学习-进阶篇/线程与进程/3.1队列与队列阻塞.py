# 队列
import queue

# 1.创建一个队列对象并取数据
a = queue.Queue()
a.put(1)     # 存数据
a.put(2)     # 存数据
a.put("3")   # 存数据
a.put(6)     # 存数据
a.put(-1)    # 存数据

# 当然队列取数据也是按照顺序取数据
b = a.get()  # 取数据,取一个数据少一个数据
print(b)
b = a.get()  # 取数据
print(b)
b = a.get()  # 取数据
print(b)
b = a.get()  # 取数据
print(b)
print('\n')



# # 2.队列的阻塞：(常见案例1)
# import queue
# import time
# import _thread
#
# def insert_queue_data():
#     time.sleep(3)
#     c.put(3)
#
# c = queue.Queue()  # 1.创建一个队列
# c.put(1)
# c.put(2)
#
#
# _thread.start_new_thread(insert_queue_data, ())  # _thread.start_new_thread表示打开另外一个线程,可以对比本章第一节内容
# while True:   # 如果队列中已经没有数据可以取了，那么这个无限循环会堵塞，无法再进行下去
#     print(c.get())
#     print("以此循环")
#
# print('\n')



# 3.队列的阻塞  (常见案例2，把2注掉后运行)
from queue import Queue

# 3 表示最大任务数为3，队列能存储的数据最多3个，如果更多数据存储，需要等取出数据
d = Queue(3)

while True:
    d.put("hello world!")
    print("存储完毕")

# 答案:
# 存储完毕
# 存储完毕
# 存储完毕








