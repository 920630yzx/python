import csv

def writeCsv(path,data):  # 注意：该函数可用于csv，txt，python文件，不能用于读取excel；写入后会覆盖原来的文件
    with open(path, "w") as f:
        writer = csv.writer(f)  # csv.writer是写入方法
        for rowData in data:  # 遍历每一行
            print(rowData)
            writer.writerow(rowData)  # writer.writerow方法完成每一行的写入

path = r"G:\pycharm\pycharm学习-进阶篇\文件读写\abc.txt"
writeCsv(path, [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])

"""
doc
docx
ppt
pdf
课下   pip
"""
