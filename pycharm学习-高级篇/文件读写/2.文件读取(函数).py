#读取csv文件
import csv
"""
是否需要传参
是否需要返回  返回值
"""
def readcsv(path):  # 注意：该函数可用于csv，txt，python文件，不能用于读取excel
    infoList = []  # 定义一个列表
    with open(path, "r") as f:
        #reader()---->f
        allFileInfo = csv.reader(f)
        for row in allFileInfo:  # 遍历每一行
            infoList.append(row)
    return infoList

path = r"G:\pycharm\pycharm学习-进阶篇\文件读写\abc.txt"
info = readcsv(path)
print(info)