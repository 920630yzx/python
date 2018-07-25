# # # 1.将文件中的每一行都读取到内存当中，存储在列表lines中
file = open("中英文对照表.txt", "r", encoding="utf-8")
lines = file.readlines()

for i in lines:
    print(i)

# 2.作业：通过解析这个文件，获取中英文数据，实现英汉字典，输入英文即可打印对应的中文
# 读取字符串
# 编写一个英汉字典
file = open("中英文对照表.txt", "r", encoding="utf-8")

lines = file.readlines()  # readlines 表示把文件的每一行当成一个字符串来读取，然后放在一个列表中

dictionary = {}

for i in lines:
    line_list = i.split("\t")    # i.split 将字符串分割,有空格就分割，返回一个列表,"\t为水平制表
    dictionary[line_list[0]] = line_list[1]

print(dictionary)

''' 添加字典
while True:
    eng = input()
    print(dictionary[eng])'''







