# 10.Spinbox滑轮
import tkinter
window = tkinter.Tk()
window.title("qianfeng")
window.geometry("400x400+200+20")

def updata():
    print(v.get())

v = tkinter.StringVar()  #绑定一个变量
sp = tkinter.Spinbox(window, from_=0, to=100, increment=2, textvariable=v, command=updata).pack()   # tkinter.Spinbox()创建Spinbox
# 或者sp.pack()
# from_=0, to=100表示按钮(或者指针)起始值和终值；increment=1表示步长。
v.set(20)  # 设置初始值
window.mainloop()  # 进入消息循环mainloop



# 11.下滑菜单栏  tkinter.Menu()
import tkinter
window = tkinter.Tk()
window.title("qianfeng")
window.geometry("400x400+200+20")

menubar = tkinter.Menu(window)  # tkinter.Menu表示创建菜单条(位于首上)！！！
window.config(menu=menubar)   # 创建菜单条(位于首上),关联作用！！！

def func():
    print("你是一个好人！")

menu1 = tkinter.Menu(menubar,tearoff=False)  # tkinter.Menu创建菜单选项；tearoff=False表示开头没有分割线，若不写则默认开头有分割线
for item in ["python", "c", "oc", "c#", "java", "js", "php", "退出"]:  # 给菜单添加内容（二级目录）
    if item == "退出":
        menu1.add_separator()  # 添加一个分割线，这个分割线在"退出"栏的上面！！！
        menu1.add_command(label=item, command=window.quit)  # window.quit表示关闭窗口，window.quit是window的一个内置函数
    else:
        menu1.add_command(label=item, command=func)  # command=func，func是已经封装好的函数

menubar.add_cascade(label="语言", menu=menu1)  # menubar.add_cascade向菜单条中添加菜单选项(一级目录)，menu1的名称为"语言"！！！
menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="blue")
menubar.add_cascade(label="颜色", menu=menu2)   # 向菜单条中添加菜单选项(一级目录)，menu1的名称为"颜色"
window.mainloop()  # 进入消息循环mainloop



# 12.右键-下滑菜单栏  tkinter.Menu()
import tkinter
window = tkinter.Tk()
window.title("qianfeng")
window.geometry("400x400+200+20")

menubar = tkinter.Menu(window)   # tkinter.Menu表示创建菜单条(位于首上)！！！
menu = tkinter.Menu(menubar, tearoff=False)  # tkinter.Menu创建菜单选项

for item in ["python", "c", "oc", "c#", "java", "js", "php", "退出"]:  # 给菜单添加内容（二级目录）
    menu.add_command(label=item)  # add_command添加二级菜单

menubar.add_cascade(label="语言", menu=menu)   # menubar.add_cascade向菜单条中添加菜单选项(一级目录)；其名称为"语言"，菜单选项为menu列表中的内容

def showMenu(event):
    menubar.post(event.x_root, event.y_root)

window.bind("<Button-3>",showMenu)  # window.bind表示绑定，"<Button-3>"表示右键。即右键与showMenu绑定，点击右键则显示菜单showMenu。
window.mainloop()   # 进入消息循环mainloop

