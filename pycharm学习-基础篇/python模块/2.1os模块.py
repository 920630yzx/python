#-*- coding:utf-8 -*-
import sys

import os
print(os.name)  # 获取当前系统；如果是 mac os /Linux 获取到的就是 posix ;如果是window 电脑得到的就是 nt

path = os.getcwd()  # 获取当前路径的方法,注意这里是绝对路径
print(path)   # 获取当前路径的方法,注意这里是绝对路径

print(os.environ)   # 获取系统环境变量

print(os.environ.get('C:\\ProgramData'))    # 获取环境变量里面的内容

print(os.listdir(os.getcwd()))   # 获取文件夹(这个文件夹)下面的所有文件,注意path写绝对路径【os.getcwd()是绝对路径】

'''
# 绝对路径: 就是从你计算机的第一层开始算起
# 相对路径: 相对于你当前的文件夹来说的
os.mkdir("login")   # 创建文件夹,默认为当前路径
os.rename("login", "login1")   # 重命名文件夹，将"login"改为"login1"
os.mkdir(os.getcwd()+"/login")  # 使用绝对路径创建文件夹,os.getcwd()为当前路径【这里是绝对路径】，"/login"为文件名
os.rename(os.getcwd()+"/login", os.getcwd()+"/login1")   #  使用绝对路径进行修改文件名,os.getcwd()为当前路径【这里是绝对路径】
os.removedirs(os.getcwd()+"/login1")  # 删除文件夹
os.remove(os.getcwd()+"/test.py")   # 删除文件
os.remove("test.py")   # 用相对路径(一般是当前的路径)删除文件 '''

'''
print(os.path.isabs("fors.py"))  # 判断是不是绝对路径，如果不是绝对路径返回 False 如果是绝对路径返回True
print(os.path.isabs(os.getcwd()+"/fors.py"))   # 写一个绝对路径
print(os.path.isfile(os.getcwd()+"/fors.py"))  # 判断是不是文件,fors.py为文件名,os.getcwd()+为当前路径【这里是绝对路径】
print(os.path.isfile("fors.py"))  # 判断是不是文件,fors.py为文件名,与上面的不同之处在于使用的相对路径【一般是该路径下】
print(os.path.isdir(os.getcwd()+"/login"))  # 判断是不是文件夹,login为文件名,os.getcwd()+为当前路径【这里是绝对路径】
print(os.path.basename(os.getcwd()+"/fors.py"))  # 返回名字
print(os.path.splitext(os.getcwd()+"/fors.py"))  # 返回文件后缀,返回是元祖
print(os.path.getsize(os.getcwd()+"/文件读写"))   # 返回文件大小
print(os.path.exists(os.getcwd()+"/文件读写"))  # 判断文件存在不存在,存在返回True 不存在的时候 false
print(os.path.split(os.getcwd()+"/文件读写") )  # 切割路径与文件名字
print(os.path.dirname(os.getcwd()+"/文件读写"))  # 获取文件夹的直接路径 '''

# os 模式还可以执行linux 命令,同时可以执行shell脚本,基本的linux命令包括：
# ls 查看所有文件
# cd 进入下一层目录
# ls -l 查看文件权限
# mkdir 创建文件夹
# 777 原则 第一个7就是自己可读可写可执行 第二个group可读可写可执行 第三其他   r = 4 w = 2 x = 1
#os.system("ls")  # 展示当前文件
#os.system("ls -l")  # 查看文件夹的权限
# os.system("chmod 777 login")  # 执行chmod 777 文件名字
# os.system("ls -l")  # 展示权限
# os.system("sh login.sh")  # 执行shell脚本，shell是门语言，以.sh结尾的语言。



# 实战项目,遍历指定路径(G:\pycharm\pycharm学习-进阶篇\面向对象的程序设计),返回其文件(当然不是文件夹)
import os
print(os.listdir(os.getcwd()))  # 获取当前文件夹一级目录的全部文件
print('\n')

# 进行判断如果是文件我们就加入到list里面,否则调用本身继续进行递归
def dirlist(path,alllist):
    filelist = os.listdir(path)  # 通过 os模块获取所有的
    for filename in filelist:    # 使用for循环遍历
        filepath = os.path.join(path,filename)
        if os.path.isdir(filepath) :
            dirlist(filepath,alllist)
        else:
            alllist.append(filepath)
    return alllist

print(dirlist("G:\pycharm\pycharm学习-进阶篇\面向对象的程序设计",[]))









