from pymongo import MongoClient


conn = MongoClient("localhost", 27017)    # 连接服务器
db = conn.mydb    # 连接数据库，mydb为数据库名称
collection = db.student_2  # 获取集合，student_2为集合名称，student_2不存在则自动创建一个

# 添加文档
# collection.insert({"name":"abc", "age":19, "gender":1,"address":"北京", "isDelete":0})
collection.insert([{"name":"abc1", "age":19, "gender":1,"address":"上海", "isDelete":0},{"name":"abc2", "age":19, "gender":1,"address":"成都", "isDelete":0}])

# 断开
conn.close()