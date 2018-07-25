# 时间戮
import time
print(time.time())  # 通常时间表示从1970年1月1日00：00：00开始以秒为单位，返回的是一个float型数据
print(type(time.time()))  # 通常时间表示从1970年1月1日00：00：00开始以秒为单位，返回的是一个float型数据

print(time.clock())  # 函数以浮点数计算的秒数返回当前的CPU时间,用来衡量不同程序的耗时

'''
符号             简述
%a       本地简化的星期的名称
%A       本地完整的星期的名称
%b       本地简化的月份的名称
%B       本地完整的月份的名称
%c       本地相应的日期的表示和时间表示
%d       月内的一天(0-31)
%H       24小时(0-23)
%I       12小时(0-12)
%J       年内的一天(1-365)
%m       月份(1-12)
%M       分钟(00-59)
%s       秒(00-59)
%y       两位数的年份表示(00-99)
%Y       四位数的年份表示(00-9999)
'''

'''
元组（struct time）:共有9个属性
索引        属性             值
0         tm_year(年)       2018
1         tm_mon(月)        1-12
2         tm_mday(日)       1-31
3         tm_hour(时)       0-23
4         tm_min(分钟)      0-59
5         tm_sec(秒)        0-61 ！
6         tm_wday(星期)     0-6 ！
7         tm_yday(时)       1-366  #一年中的第几天
8     tm_isdst(是否是夏令时)默认值为-1，结果1表示是，0表示否
'''

# 1.UTC(世界协调时):格林威治天文时间,世界的标准时间   中国:   UTC+8
# 1.localtime:获取当前时间的struct_time形式
print(time.localtime())  # 以元组为标准得到9个属性  #例如：time.struct_time(tm_year=2018, tm_mon=5, tm_mday=30, tm_hour=13, tm_min=44, tm_sec=27, tm_wday=2, tm_yday=150, tm_isdst=0)

# 2.获取当天的时间
import datetime
print(datetime.datetime.now())  # 当天详细时间
print(datetime.date.today())  # 当天时间

# step2：获取昨天的日期
def getTesterday():
    today = datetime.date.today()  # 获取当天时间
    oneday = datetime.timedelta(days=1)  # ays=1,表示时间跨度为1天
    yesterday = today - oneday
    print(yesterday)
    return yesterday
yesterday = getTesterday()
print("昨天的时间为：", yesterday)


# 3.转换时间和日期的格式
import time
import datetime

def strTodaytime(datestr,format):  # datestr为对应时间
    return datetime.datetime.strptime(datestr,format)  # datetime.datetime.strptime函数

print(time.strftime("%y-%m-%d ",time.localtime()))  # time.strftime表示格式转换,"%Y-%m-%d %H:%M:%S"格式见上面详细说明 ！！！  18-05-30
print(time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))  # time.strftime表示格式转换,"%Y-%m-%d %H:%M:%S"格式见上面详细说明 ！！！  18-05-30 14:13:36
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # time.strftime表示格式转换,"%Y-%m-%d %H:%M:%S"格式见上面详细说明 ！！！  2018-05-30 14:13:36
print(strTodaytime("2014-2-16", "%Y-%m-%d"))  # 结果为2014-02-16 00:00:00
print('\n')


# 4.获取日历相关的信息
import calendar
# 获取个月的日历，返回字符串的类型
cal = calendar.month(2015, 12)  # 获取2015年12月的日历
print(cal)

# 获取一年的日历
cal = calendar.calendar(2018)
print(cal)

# 设置日历的第一天
calendar.setfirstweekday(calendar.SUNDAY)  # 以星期天为第一列输出日历，当然默认是以星期一为第一天
cal = calendar.month(2015, 12)
print(cal)

# step2: 得到日历的HTML格式,当然这个一般是用不了的
cal = calendar.HTMLCalendar(calendar.MONDAY)
print(cal.formatmonth(2015, 12))








