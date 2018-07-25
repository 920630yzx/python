# 【列表】当需要存储大量的数据，需要声明一个列表，列表会分配给每个数据一个索引（编号）
# 1.创建列表
list1 = ["张三", "李四", "王五", "赵六"]
list2 = [1, 2, 3, 4]
list3 = ["hahaha", 12, True]

print(list1, list2, list3)

#2.访问列表
print(list1[0], list1[1], list1[2])

#3.确定列表的元素个数
print(len(list1))  #列表的长度即是列表字符串的个数

#4.遍历列表中的每个元素
for i in list1:
    print(i)

#5.列表修改
originList = [0, 1, 2, 3, 4, 5]
#step1：增
#追加元素:  append()函数
originList.append(6)
print(originList)
#方法2,直接增加:
newList = originList + [7]
print(newList, originList)

#批量增加元素  extend()函数
originList = [0, 1, 2, 3, 4, 5]
originList.extend([6, 7, 8, 9])
print(originList)
#方法2,直接增加:
newList = originList + [6, 7, 8, 9]
print(newList, originList)

#step2:插入  insert()函数
originList = [0, 1, 2, 3, 4, 5]
originList.insert(3, True)  #在位置3之前加入True这个字符
print(originList)

# step3：删
originList = [0, 1, 2, 3, 4, 5]
originList.clear()  # 全部删除
print(originList)

originList = ["a", "b", "c", "b", "d"]
originList.remove("b")  # 从左至右,删除第一个匹配的元素
print(originList)

originList = ["a", "b", "c", "d", "e"]
del originList[2]  # 根据索引进行删除,c被删除
print(originList)


# step4:改
# 逆向  reverse()函数
originList = ["a", "b", "c", "d", "e"]
originList.reverse()
print(originList)
originList[2] = "T"  # 根据索引进行修改,c修改为T
print(originList)

# step5:查   .index("b")函数;[]直接索引查找
originList = ["a", "b", "c", "d", "e", "b"]
# 查找列表中第3个元素
e = originList[3]
print(e)  # 也就是d
# 查找列表中是否存在"b"，位置在哪里
index = originList.index("b")
print(index)  # 答案为1

# 6.分割字符串,生成的小字符串,就是放在列表中的
var = "I am a good man"
x = var.split(" ")  # var.split()也可
print(x)

# 7.将列表中的小字符串拼接
var = "*"  # 以*符号为分隔符
newVar = var.join(x)
print(newVar)

# 8.列表的遍历
# 【注】相对于声明大量的变量，由于列表为每个元素设置了索引，因此可以方便的通过循环
# 批量处理
strList = ["abc", "exf", "ery"]
newStrList = []
for i in strList:  # i依次遍历strList
    newStrList.append(i.upper())  # 给newStrList依次添加
print(newStrList)

for i in range(0, len(strList)):
    if i >= 1:  #从编号为1的字符串开始修改
        strList[i] = strList[i].upper()  #upper函数不会改变原列表
print(strList)
print(len(strList)) #答案为3
print('\n')







#【元组】看上去有点像列表，但实际上元祖表示的是复合的单一数据
# 假如我要管理一个学员的信息，包括姓名，年龄，背景，学历
student0 = ("张三", 18, "群众", "本科")  # 创建元祖

studentsList = [("张三", 18, "群众", "本科"),
                ("李四", 19, "党员", "本科"),
                ("王五", 27, "群众", "研究生")]  # 本身是列表，内含3个元组

print(student0[0])
print(type(student0))
print(len(student0))
print(type(studentsList))
print('\n')


