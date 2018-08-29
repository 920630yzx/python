# # 注意1，2，3不要同时运行
# # 1.读取完一张表返回整体的数据   # 注意：只能用于读取Xlsx
# from openpyxl.reader.excel import load_workbook
#
# def readXlsxFile(path):   # 注意：只能用于读取Xlsx
#     dic = {}   # 定义字典，用于存储数据
#     file = load_workbook(filename=path)  # 打开文件
#     sheets = file.get_sheet_names()  # 获取所有表格的名称
#     for sheetName in sheets:  # 遍历表格
#         sheet = file.get_sheet_by_name(sheetName)  # 获取具体表格数据
#         sheetInfo = []  # 定义列表
#         for lineNum in range(1, sheet.max_row + 1):  # 遍历行
#             lineList = []  # 定义列表
#             for columnNum in range(1, sheet.max_column + 1):   # 遍历列
#                 value = sheet.cell(row=lineNum, column=columnNum).value  #  sheet.cell函数表示获得文件指定单元格的数据；row=lineNum,column=columnNum分别表示行和列
#                 lineList.append(value)  # 储存一行的数据
#             sheetInfo.append(lineList)  # 储存多行的数据(一行变多行)
#         dic[sheetName] = sheetInfo  # 将一张表的数据存储到字典中,储存一张表
#     return dic
#
# path = r"G:\report.xlsx"
# dic = readXlsxFile(path)
# print(dic["summary"])  # 打印"summary"页



# # 2.读取完一张表并返回整体的数据,这里既可以读取lsx也可用于读取xls，这种方式明显更简单
# """
# pyexcel_xls  当然需要导入pyexcel_xls模块：pip install pyexcel_xls
# """
# from pyexcel_xls import get_data
# from collections import OrderedDict  # 有序的字典，一种特殊的处理方式
# def readXlsAndXlsxFile(path):  # 注意：如果在该模块中使用中文，编码为unicode，需要编码转换以防乱码
#     dic = OrderedDict()  # 有序字典
#     xData = get_data(path)  # 抓取数据
#     for sheet in xData:
#         dic[sheet] = xData[sheet]
#     return dic
#
# path = r"G:\report.xlsx"
# dic = readXlsAndXlsxFile(path)
# print(dic)



# 3.向xls文件中写入数据(有序字典)
from collections import OrderedDict
from pyexcel_xls import save_data

def makeExcelFile(path,data):
    dic = OrderedDict()  # 调用有序字典
    for sheetName, sheetValue in data.items():  # 字典遍历：data.items()同时获取data.keys和data.values
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)

    save_data(path, dic)

path = r"G:\report2.xls"
makeExcelFile(path, {"Sheet1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]], "Sheet2": [[11, 22, 33], [44, 55, 66], [77, 88, 99]]})
# "Sheet1","Sheet2"分别是两张表的表名


