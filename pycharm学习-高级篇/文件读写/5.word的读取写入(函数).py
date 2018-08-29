
"""
第三方文件：win32com
"""
import win32com
import win32com.client
import os

# 1:写入word       运行下面这段话请将'2.读取word'注解掉，最好不要一边写入一边读取
def makeWordFile(path,name):
    word = win32com.client.Dispatch("Word.Application")  # 连接固定的文档
    word.Visible = True  # 让文档可见
    doc = word.Documents.Add()  # 创建一个文档
    r = doc.Range(0, 0)  # 写内容，从头到尾写入
    r.InsertAfter("亲爱的"+name+"\n")
    r.InsertAfter("    我想你啦....^_^")
    doc.SaveAs(path)  # 存储文件
    doc.Close()  # 关闭文件
    word.Quit()  # 退出word


names = ["老王", "小王", "老宋"]
for name in names:
    # 例如   os.path.join(D:\name\zhen,xiao) ==   D:\name\zhen\xiao
    path = os.path.join(os.getcwd(), name)  # os.path.join里面的两个参数组合成一个新的路径，‘/’会自动添加；os.getcwd()是当地路径，name是文件名。
    makeWordFile(path, name)



# 2.读取word：       运行下面这段话请将上面注解掉，最好不要一边写入一边读取
def readWordFile(path):
    # 调用系统word功能，可以处理doc和docx两个文件
    mv = win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc = mv.Documents.Open(path)
    # 遍历doc文件的段落
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    doc.Close()  # 关闭文件
    mv.Quit()  # 退出word

path = r'F:\mv.doc'  # word文档的地址
readWordFile(path)  # 调用函数

































