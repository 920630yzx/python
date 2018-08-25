from pymongo import MongoClient

conn = MongoClient("localhost", 27017)  # 连接服务器
db = conn.mydb  # 连接数据库
collection = db.abc   # 获取集合

collection.remove({"name":"lilei"})

collection.remove()   # 全部删除，不写条件就是全部删除
conn.close()  # 断开















