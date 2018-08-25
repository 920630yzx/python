# 13.下拉控件Combobox
import tkinter
from tkinter import ttk  # 引入ttk模块

window = tkinter.Tk()
window.title("qianfeng")
window.geometry("400x400+200+20")

cv = tkinter.StringVar()  # 绑定一个变量
com = ttk.Combobox(window, textvariable=cv)  # ttk.Combobox创建下拉菜单！！！
com.pack()

com["value"] = ("黑龙江", "吉林", "辽宁")  # 设置数据
com.current(0)  # 设置默认值，即默认值（初始值）是"黑龙江"

def func(event):  # 通过.get()获取数据！
    print(com.get())
    print(cv.get())

com.bind("<<ComboboxSelected>>", func)   # com.bind绑定事件，"<<ComboboxSelected>>"表示下拉控件！！！
window.mainloop()  # 进入消息循环mainloop



# 14.树状结构 Treeview   （即树状图）
from tkinter import ttk
import tkinter

window = tkinter.Tk()
window.title("qianfeng")
window.geometry("400x400+200+20")

tree = ttk.Treeview(window)  # ttk.Treeview创建树状结构！！！
tree.pack()

# 添加一级树枝：  这里"中国"和values=("F1")好像不太重要；0，1，2表示菜单的先后顺序
treeF1 = tree.insert("", 0, "中国", text="中国CHI", values=("F1"))  # ""：是因为一级菜单前面为空；text是文本，values是具体的值
treeF2 = tree.insert("", 1, "美国", text="美国USA", values=("F2"))
treeF3 = tree.insert("", 2, "英国", text="英国ENG", values=("F3"))

# 添加二级菜单：
treeF1_1 = tree.insert(treeF1, 0, "黑龙江", text="中国黑龙江", value=("F1_1"))  # treeF1表示该二级菜单在treeF1下面
treeF1_2 = tree.insert(treeF1, 1, "辽宁", text="中国辽宁", value=("F1_2"))     # treeF1表示该二级菜单在treeF1下面
treeF1_3 = tree.insert(treeF1, 2, "吉林", text="中国吉林", value=("F1_3"))    # treeF1表示该二级菜单在treeF1下面

treeF2_1 = tree.insert(treeF2, 0, "德克萨斯州", text="美国的德克萨斯州", value=("F2_1"))  # treeF2表示该二级菜单在treeF2下面
treeF2_2 = tree.insert(treeF2, 1, "底特律", text="美国底特律", value=("F2_2"))   # treeF2表示该二级菜单在treeF2下面
treeF2_3 = tree.insert(treeF2, 2, "旧金山", text="美国旧金山", value=("F2_3"))   # treeF2表示该二级菜单在treeF2下面

# 三级菜单：
treeF1_1_1 = tree.insert(treeF1_1, 0, "哈尔滨", text="黑龙江的哈尔滨")  # treeF1_1表示该三级菜单在treeF1_1下面
treeF1_1_2 = tree.insert(treeF1_1, 1, "五常", text="黑龙江五常")      # treeF1_1表示该三级菜单在treeF1_1下面

window.mainloop()  # 进入消息循环mainloop