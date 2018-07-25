# 【字典】字典是编程中常见的数据结构，字典像列表一样存储大量的数据，但是字典中的数据
# 没有编号没有索引，每个数据作为字典中的一个值，每个值有一个对应的键，形成键值对，
# 通过键，查找值，而不是通过索引

dictionary0 = {"One" : 1, "Two" : 2, "Three" : 1}
# "One" 和 1组成一个键值对，“One”是键key，1是值value
# 键是已知的，通过键，查找值
# 值是可以重复的，每个键都是唯一的
print(dictionary0["One"])

wellcomeDict = {
    "ENG": "Welcome",
    "CHA": "欢迎"
}
print(wellcomeDict["CHA"])

hotKeyDict = {
    "丢枪": "F",
    "下蹲": "C"
}

hotKeyDict["丢枪"] = "T"

print("请按" + hotKeyDict["丢枪"] + "键丢枪")
print('\n')

# 1.定义字典
dict1 = {"One": 1, "Two": 2, "Three": 3}
print(dict1)

# 2.字典元素的增加和删除   update()函数
dict1.update({"Four": 4, "Five": 5})
print(dict1)

# 3.找出字典所有的key   keys()函数
keyList = dict1.keys()
# 字典中取出的key，就是dict_keys
print(keyList)
print(type(keyList))
print(list(keyList)[0]) #取出第一个字典的名称


# 4.判断一个key是否已经出现在字典中
if "One" in dict1:
    print("在")

# 5.找出字典中所有的键值对   items()函数
# x的类型是dict_items可以转成列表使用，列表的元素是包含键值对的元组
dict1 = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
x = dict1.items()
print(x)
print(list(x)) #转成列表,列表的元素是包含键值对的元组
print('\n')

# 集合
# 集合和列表非常接近，但是集合中的元素是不能重复的，而且集合并不考虑元素的位置，或索引
# 集合只是限制一个范围，只用来判断一个值是否出现在这个范围内
# 6.集合作用就是对元素范围的交集,补集运算,定义集合：
set1 = {0, 1, 2, 3, 4, 4}
# 集合的元素不能重复，重复也没有意义
if 0 in set1:
    print("是的")

# 集合的元素也可以是任何数据
# 如果集合的元素是字符串，列表，字典中的数据，是可以强转的   set()函数可以将其转换成集合
set2 = set(", !:.")
print(set2)
print(set2, set1)

A=[1, 2, 3, 3, 4, 5, 1]
set3 = set(A)  #set()函数可以将其转换成集合,同时去掉同值
print(set3)

# 7.集合的计算
set1 = {0, 1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
# 求交集
newSet = set1 & set2   # &求交集，也读作“与”
print(newSet)
# 求并集
newSet = set1 | set2   # |求并集，也都做“或”
print(newSet)
# 求补集
newSet = set1 ^ set2   # ^求补集，也读作“异或”
print(newSet)
# 求差集 求set1当中有，set2中没有的
newSet = set1 - set2   # -求差集，读作“减”
print(newSet)





