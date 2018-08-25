from pymongo import MongoClient

conn = MongoClient("localhost", 27017)  # 连接服务器
db = conn.mydb  # 连接数据库
collection = db.student  # 获取集合

collection.update({"name":"lilei"},{"$set":{"age":25}})
# 断开
conn.close()
