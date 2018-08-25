"""
网络版的英汉词典：要求联网，必须要在有网的环境  xpas5.0网站
注册;账号，密码  key
w网络：
    网络请求：
        get
        post
    响应：
解析：
    parse
json--->String
xml
"""
from tkinter import *  #  '*'这个表示导入tkinter下的所有模块
import urllib.request as ur
from urllib.parse import quote
import json

root = Tk()   # 创建主窗口
root.title("英汉词典")  # 设置标题title
root.geometry("500x500")  # 设置大小;"500x500"表示初始化主窗口的大小.
root.resizable(width=True, height=False)  # 设置高度和宽度

# 将数据设置到列表
def setData(listData):
    resultList.delete(0, END)  # 清空之前的数据！！！从头到尾
    if isinstance(listData, list):
        for item in listData:
            resultList.insert(END, item['pos'] + '  '+item['def'])
    else:
        resultList.insert(END, listData)

# api查询数据设置：  ！！！
def queryDict(word):
    url = 'http://xtk.azurewebsites.net/BingDictService.aspx?Word='+quote(word)  # 确定查询地址  quote(word)来传单词
    with ur.urlopen(url) as f:  # 连接，发送请求；进行在线解析
        listData = f.read().decode()  # 拿到数据
        try:
            module = json.loads(listData)['defs']  # 解析json；用try防止发生异常；'defs'是文字格式
            setData(module)
        except ValueError as e:
            setData(listData)

# 输入框的布局：
inputFrame = Frame(root, height=15)  # Frame输入框的布局 ！！！
entry = Entry(inputFrame, width=30, font=10)  # Entry创建输入框,依附于inputFrame窗口！！！
entry.pack(side=LEFT, padx=20, pady=50)  # side=LEFT表示放在左边；padx=20,pady=50是x和y的位置

# 按钮布局：
button = Button(inputFrame, text="查询", command=lambda: queryDict(entry.get()))  # 创建按钮,依附于inputFrame窗口；text="查询"是文本；entry.get()是获取内容！！！
button.pack(side=LEFT)  # side=LEFT表示放在左边！！

inputFrame.pack(expand=NO, fill=X)  # fill=X填满X轴，这样可以横着排；！！

# 查询结果布局：
resultFrame = Frame(root, height=300, width=400, bg="white")  # Frame输出框的布局 ！！！

# 列表
resultList = Listbox(resultFrame)  # 与resultFrame进行关联
resultList.pack(fill=BOTH, expand=NO)  # fill=BOTH全部填满！！
resultFrame.pack(fill=BOTH, expand=NO, padx=20)  # padx=20
root.mainloop()  # 进入消息循环mainloop




























