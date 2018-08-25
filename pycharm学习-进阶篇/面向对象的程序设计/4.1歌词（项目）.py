# 歌词解析程序
# 歌词管理器 <> 词句

import time
import os


# 建立数据模型，储存一句歌词的相关信息
class LrcItem:
    time = 0.0      # 以秒为单位的时间
    seg = ""  # 一句歌词

    def __init__(self, time, seg):
        self.time = time
        self.seg = seg


# 歌词管理器，负责通过时间获取歌词
class LrcManager:
    lrcList = []

    # 设置歌词路径
    def set_lrc_path(self, path):
        self.lrcList = []  # 清空作用
        # 打开歌词文件
        lines_list = self.open_lrc_file(path)
        # 解析歌词，创建歌词对象，存储数据
        self.anazy_lines(lines_list)
        # 根据时间排序
        self.sort_lrc_items()

    def open_lrc_file(self, path):
        file = open(path, "r")
        return file.readlines()

    def anazy_lines(self, lines_list):
        for line in lines_list:
            self.anazy_line(line)

    def anazy_line(self, line):
        l = line.split("]")   # [00:00.00] 用右括号进行拆分
        if l[1] == "":  # 没有I[1]，I[1]不存在则直接返回
            return
        # 建立模型
        ret = self.get_time_from_string(l[0])  # l[0]表示时间,获取之
        if ret:  # 或者写成 if ret！= None，表示如果ret为真
            lrc_item = LrcItem(ret, l[1])  # LrcItem不在本类里,所有没有self.
            self.lrcList.append(lrc_item)

    def get_time_from_string(self, string):
        # [03:20.08  [ti
        m = string[1:3]  # 获取分
        s = string[4:]  # 获取秒
        if not m.isdigit():  # 如果不是全数字,则返回，可以看看双截棍前面部分，存在分钟不是全数字的情况
            return None
        return int(m) * 60 + float(s)  # 返回总的秒数

    # 对歌词进行排序 时间从大到小   # 冒泡排序法，了解下，以后遇到也基本是一样的
    def sort_lrc_items(self):
        for i in range(0, len(self.lrcList)):
            for j in range(0, len(self.lrcList) - i - 1):
                if self.lrcList[j].time < self.lrcList[j + 1].time:  # 比较时间，永远把小的放在后面
                    item = self.lrcList[j]
                    self.lrcList[j] = self.lrcList[j + 1]
                    self.lrcList[j + 1] = item

    def show_lrc_items(self):  #循环打印
        for item in self.lrcList:
            print(item.time, item.seg)

    # 根据给的时间返回歌词
    def get_lrc_for_time(self, t):  # 注意时间从大到小排序
        for item in self.lrcList:
            if item.time < t:
                return item.seg   # 结束函数并返回歌词
        return ""  # 给的时间太小，不返回任何东西


lrc = LrcManager()
lrc.set_lrc_path("周杰伦双截棍(Live).lrc")

# lrc.show_lrc_items()

t = 0
while True:
    time.sleep(1)
    x = os.system('cls')
    t += 1
    print(lrc.get_lrc_for_time(t))

