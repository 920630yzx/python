# 异常处理
# 编程过程中可能出现很多的错误，导致程序崩溃，其实程序崩溃是操作系统和解释器，故意让程序崩溃的；为了防止更大错误出现
# 当崩溃的时候，操作系统或者解释器会发出一个异常信息，我们可以捕获这个异常信息，进行一次补救。

# try:
#     a = input()
#     print(int(a) + 1)
# except ValueError:
#     print("异常信息")
# except IOError:
#     print("IOError")
# except EOFError:
#     print("EOFError")

try:
    a = input()
    print(int(a) + 1)

except Exception as error:  # error指代错误，Exception错误的名称；Exception表示所有异常类的基类，可以捕获所有的错误信息。
    print("异常信息", error, type(error))

# 当然也可以换成 except：
#                        print('错误')

