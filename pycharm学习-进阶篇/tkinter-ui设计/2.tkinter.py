# 6.带滚动条的Text (接上一节)
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20") # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置

scroll = tkinter.Scrollbar()  # 创建一个滚动条
text = tkinter.Text(window, width=50, height=8)  # side放到窗体的哪一侧，fill填充；tkinter.Text表示定义文本框，width=300, height=10表示长度及宽度！！！

scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)  # scroll.pack设置滚动条；side=tkinter.RIGHT, fill=tkinter.Y表示放在右侧并填满Y轴
text.pack(side=tkinter.LEFT, fill=tkinter.Y)  # text.pack设置文本框

scroll.config(command=text.yview)  # 关联config,将scroll与text相关联；command=text.yview表示y轴显示
text.config(yscrollcommand=scroll.set)

str = "asgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklfasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklf" \
      "lasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklfllgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdl" \
      "gsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhjasgjkfjdklflgsakdlgsdkjfjksdhj"

text.insert(tkinter.INSERT, str)  # text.insert 表示插入字符串,同时还可在运行后的文本框中继续添加字符！！！

window.mainloop()  # 进入消息循环mainloop



# 7.checkButton多选框控件
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20")  # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置window = tkinter.Tk()  # 创建主窗口

def updata():
    message = ""
    if hobby1.get() == True:  # 如果hobby1存在
        message += "money\n"  # money是具体内容
    if hobby2.get() == True:
        message += "power\n"  # power是具体内容
    if hobby3.get() == True:
        message += "people\n"  # people\是具体内容

    # 需要清除text中所有的内容,text.delete：
    text.delete(0.0, tkinter.END)  # text.delete表示清除text；(0.0, tkinter.END)表示范围从开始到结束
    text.insert(tkinter.INSERT, message)   # text.insert 表示插入字符串；message是加入的内容

hobby1 = tkinter.BooleanVar()   # tkinter.BooleanVar()表示要绑定的数据
check1 = tkinter.Checkbutton(window, text="money", variable=hobby1, command=updata)   # tkinter.Checkbutton表示创建多选框；variable=hobby1表示将其绑定(框与数据)
check1.pack()

hobby2 = tkinter.BooleanVar()  # 要绑定的数据BooleanVar()
check2 = tkinter.Checkbutton(window,text="power", variable=hobby2, command=updata)  # 创建多选框2
check2.pack()

hobby3 = tkinter.BooleanVar()  # 要绑定的数据BooleanVar()
check3 = tkinter.Checkbutton(window, text="people", variable=hobby3,command=updata)  # 创建多选框3
check3.pack()

text = tkinter.Text(window, width=50, height=5)  # tkinter.Text表示定义文本框，width=50, height=5表示长度及宽度！！！
text.pack()

window.mainloop()  # 进入消息循环mainloop



# 8.Radio Button(单选按钮)
import tkinter

window = tkinter.Tk()  # 创建主窗口
window.title("qianfeng")  # 设置标题title
window.geometry("400x400+200+20")  # 设置大小和位置400x400表示初始化主窗口的大小，200，20初始化时窗口坐在的位置window = tkinter.Tk()  # 创建主窗口

def updata():
    print(r.get())  # r.get()表示获取

r = tkinter.IntVar()  # 一组单选按钮绑定同一个变量

radio1 = tkinter.Radiobutton(window, text="one", value=44, variable=r, command=updata)  # tkinter.Radiobutton创建单选按钮！！！
radio1.pack()
radio2 = tkinter.Radiobutton(window, text="two", value=55, variable=r, command=updata)  # text="one"表示单选框中内容;variable=r表示单选框还未被选中
radio2.pack()
radio3 = tkinter.Radiobutton(window, text="three", value=66, variable=r, command=updata)
radio3.pack()

window.mainloop()  # 进入消息循环mainloop



# 9.Scale滑轮  tkinter.Scale()
import tkinter
window = tkinter.Tk()
window.title("qianfeng")
window.geometry("400x400+200+20")

scale = tkinter.Scale(window, from_=0, to=100, orient=tkinter.HORIZONTAL, tickinterval=100, length=200)  #tkinter.Scale表示创建滑轮；from_=0, to=100表示指针范围！！！
# orient是方向;orient=tkinter.HORIZONTA表示滑轮水平，orient=tkinter.HORIZONTAL表示水平滑轮，orient=tkinter.VERTICAL表示竖直滑轮！！！
scale.pack()  # .pack()表示显示出来

scale.set(20)  # 设置默认值set,即指针初始值

def showNum():  # 设置输出值
    print(scale.get())
tkinter.Button(window,text="按钮",command=showNum).pack()  # 可以直接.pack()
window.mainloop()  # 进入消息循环mainloop