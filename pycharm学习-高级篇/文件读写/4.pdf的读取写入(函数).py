
"""
读取pdf文件
写入 txt文件

读取pdf问津需要安装第三方
pdfminer3k----->读取pdf文件
如何关联第三方
pip 第三方名称  install

"""
import sys
import importlib
importlib.reload(sys)


from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.layout import LTTextBoxHorizontal, LAParams

"""含义：
pdfparser:从一个文件中获取数据（解析数据）
PDFDocument：保存获取的数据和PDFPaeser是相互关联的
PDFPageInterpreter：处理pdf页面的内容,页面解释器
PDFResourceManager：用于存储共享数据，如字体/图像等
layout:布局    
"""

def readPDF(path,topath):
    # f = open(path, "rb")   # 以二进制的方式打开pdf文件
    f = open(path, "r")  # 方法1：打开pdf文件
    # with open(path,"r") as f:   # 方法2：打开pdf文件
    parser = PDFParser(f)  # 创建一个pdf文档的分析器（解析器）
    pdffile = PDFDocument()  # 创建pdf文档
    parser.set_document(pdffile)  # 连接分析器和文档对象
    pdffile.set_parser(parser)    # 解析
    pdffile.initialize()      # 提供初始化
    if not pdffile.is_extractable:  # 检测文档是否提供txt转换，如果没有则
        raise PDFTextExtractionNotAllowed  # 触发一个异常
    else:  # 提供txt转换；没有异常
        # 解析数据
        # 数据管理器
        manager = PDFResourceManager()  # 创建数据管理器
        laparser = LAParams()  # 创建一个PDF设备对象
        device = PDFPageAggregator(manager, laparams=laparser)  # 创建pdf页面管理器
        interpreter = PDFPageInterpreter(manager, device)  # 解释器对象

        # 开始循环处理，每一次处理一页
        for page in pdffile.get_pages():
            interpreter.process_page(page)

            layout = device.get_result()  # 获取结果
            for x in layout:    # 循环判断
                if(isinstance(x,LTTextBoxHorizontal)):
                    with open(topath, "a") as f:  # 打开文件（打开方法2，当然也可用打开方法1）
                        str = x.get_text()  # 获取数据
                        f.write(str+"\n")

path = r"G:\直播\day03\ssss.pdf"  # pdf位置
topath = r"G:\直播\day03\qq.txt"  # 输出位置
readPDF(path, topath)







































