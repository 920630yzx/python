# redis与python交互.py
import redis
r = redis.StrictRedis("localhost", port=6379, password="sunck")  # 连接

# 方法一、根据数据类型的不同，调用相应的方法
r.set("key", "value")  # 写数据
print(r.get("key"))  # 读数据

# 方法二、pipline （管道）
# 缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set("key", "apple")
pipe.set("key1", "pear")
pipe.set("key2", "peach")
pipe.execute()