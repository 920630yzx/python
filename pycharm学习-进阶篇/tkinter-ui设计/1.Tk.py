# 1.1 tkinter概述:tkinter是python标准的GUI库，完成图形化界面

'''
step1: tkinter概述:tkinter是python标准的GUI库，完成图形化界面

step2: 创建一个GUI的步骤:
1.导入tkinter模块
2.创建控件
3.指定这个控件master.即这个控件属于谁
4.告诉GM(geomtry manage)有一个控件产生

'''

#1.实现开一个简单的图形化界面
import tkinter
window = tkinter.Tk()  # 1.创建主窗口
window.title("qianfeng")    # 2.设置标题title
window.geometry("400x400+200+20")  # 3.设置大小和位置400x400表示初始化主窗口的大小，200+20表示初始化时窗口坐在的位置
window.mainloop()  # 4.进入消息循环mainloop



#2.label控件  功能：显示文本
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20") # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置

label = tkinter.Label(window, text="千锋",
                      bg="blue", fg="red",
                      font=("黑体", 20), width=10,
                      height=4, wraplength=100,
                      justify="left", anchor="center")
""" tkinter.Label()：
win：依附的窗口,必须要传
text:显示的文本内容
bg:背景色
fg:字体颜色  font:字体及字体大小  
width:宽度  height：高度 
warplength:指定text文本中多宽进行换行
justify:设置换行后的对齐方式;justify="left"表示左对齐
anchor:位置   n：北 ；  e：东  ； s：南  ；  w：西  ；  center：中
"""

# 显示出来
label.pack()  # pack:理解为一个布局管理器，可以将其理解为一个弹性容器
window.mainloop()  # 进入消息循环mainloop



# 3 Button  定义：button就是按钮,当点击按钮时发生对应的事
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20") # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置

# 创建一个Button
def func():
    print("你是一个好人！")
button = tkinter.Button(window, text="按钮", command=func, width=10, height=10)  # tkinter.Button定义按钮
button.pack()  # .pack()表示显示出来

"""
注意点：无论使用哪种控件，需要依附一个窗口
   win：依附的窗口,必须要传，无论使用哪种控件，需要依附一个窗口
   text:设置按钮文本，"按钮"为按钮名称
   command：事件,命令   注意函数名不加括号 
   width height：分别表示宽和高
"""

window.mainloop()  # 进入消息循环mainloop



# 4.点击按钮输出输入框的内容   tkinter.Entry
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20")  # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置


def showInfo():
    print(entry.get())

entry = tkinter.Entry(window)  # tkinter.Entry定义文本输入框！！！
entry.pack()
button = tkinter.Button(window, text="按钮", command=showInfo)   # tkinter.Button定义按钮！！！
button.pack()

window.mainloop()  # 进入消息循环mainloop



# 5.创建主窗口
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20") # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置

text = tkinter.Text(window, width=300, height=10)  # tkinter.Text表示定义文本框，width=300, height=10表示长度及宽度！！！
text.pack()

str = "你是一个好人"
text.insert(tkinter.INSERT, str)  # text.insert 表示插入字符串,同时还可在运行后的文本框中继续添加字符！！！

"""
text.insert:插入数据
"""

window.mainloop()  # 4.进入消息循环mainloop





