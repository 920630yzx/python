# 第24节中间部分
#  1.打印的调试(较少使用)
# """
# print():print最大的坏处，还得删除，
#
# """
# def demo(s):
#     n = int(s)
#     print(">>>n = %d" %n)  # 打印的调试
#     return 10 / n
#
# def main():
#     demo("1")  # 输入0就会报错，此时print调试就会生效,打印出错误位置
#
# main()
#
#
#
# # 2.断言的调试  （常用）
# """
# 断言：
# assert
# 格式：
# assert expression
# 等价于：
#   if not expression:
#        raise AssertionError
# """
# def demo(s):
#     n = int(s)
#     assert n != 0, "n is zero"  # "n is zero"表示错误提示；如果促发则：  AssertionError："n is zero"
#
#     return 10/n
#
# def main():
#     demo("0")
# main()
#
# # 直接使用assert的案例：
# assert isinstance("hello",int), 'you are a bitch'



# 4.logging调试
# '''
# logging:不会抛出错误，并且可以输出到文件，一般用于程序调试
# logging需要导入它的模块
# '''
# import logging
# logging.basicConfig(level=logging.INFO)  # 抛出python内部已定义的异常
# s = "0"
# n = int(s)
# logging.info('n = %d'%n)
# print(10 / n)



"""
pdb   是python中自带的一个包，为python提供一种交互源代码调试的功能；特点是单步调试，需要导入pdb模块  （常用）
"""
import pdb
def add(a,b):
    return a + b

def cal(a,b):
    # pdb.set_trace()  # 引入pdb代码片段；关键是有无这句话的差别,运行后不断点击n看看结果
    c = add(a, b)
    print(c)

if __name__ == "__main__":
    cal(3, 4)

"""
启动pdb的方式：
   1.dos-->当前目录--》python -m pdb XXX.py  # cmd下同样可以进行调试,XXX.py表示文件名
   2.pycharm   pdb.set_trace()  # pycharm中进行调试
命令              用途
next/n        执行下一行
step/s        进入函数
list/l        查看当前代码的片段
break/b       设置断点   # 这相当于左键
continue/c    继续执行程序   或者跳到下一个断点
return/r      执行代码直接到当前函数的返回
exit/q        终止或者退出
help/h        帮助
"""

