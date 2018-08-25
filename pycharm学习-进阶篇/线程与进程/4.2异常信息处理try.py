# 创建自己的异常信息


class MyError(Exception):  # 继承自Exception
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "这就我自定义的错误，怎么着吧!" + self.message  # 返回值是两者相加，如这就我自定义的错误，怎么着吧!a的值是0


a = input()

try:
    if int(a) == 0:
        raise MyError("a的值是0")  # 返回错误，程序停止
    print(3 / int(a))  # 如果不是0，例如输入的数字是3，返回的是1.0
except ValueError as error:
    print("输入的不是整数", error)
except MyError as error:
    print(error)

'''  其他案例1：
import sys
 try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise  '''

'''其他案例2： try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。例如: 
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:  
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
'''



