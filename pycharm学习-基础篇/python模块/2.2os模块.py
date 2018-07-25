
import os
"""
path:
返回值true   false
绝对路径
\转义
"""
# 1.
aa = os.path.isfile("t.py")  # 判断是不是文件,t.py为文件名,使用的相对路径【一般是该路径下】
print(aa)
bb = os.path.isfile(r"G:\pycharm\pycharm学习-进阶篇\2.2os模块.py")   # 判断是不是文件,fors.py为文件名,与上面的不同之处在于使用的绝对路径
print(bb)

# 2.项目：遍历当前文件夹的文件并输出
print('\n')
allfileList = []  # 定义一个列表
cc = os.getcwd()  # 获取当前路径的方法,注意这里是绝对路径
print(cc)

filepath = os.listdir(cc)  # 获取文件夹(这个文件夹cc)下面的所有文件,注意path写绝对路径【os.getcwd()是绝对路径】
for fileName in filepath:
    print(fileName)
    if os.path.isfile(fileName):  # 判断是不是文件而不是文件夹,(fileName为文件名),使用的是相对路径
        allfileList.append(fileName)

print('\n')
print(allfileList)


# 3.获取当前路径
print('\n')
filepath = os.path.join(os.getcwd(), "allusers.py")  # 得到"allusers.py"当前路径【好像是添加路径】
print(filepath)
print(os.getcwd())

