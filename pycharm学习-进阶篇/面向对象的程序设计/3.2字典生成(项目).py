# 编写面向对象的英汉字典
# 首先分析需求找出对象
# 字典（一个） 词条（很多很多）


# 词条类，其对象存储一个词条信息，包括英文和对应的中文，这种用于存储单一个体信息的
# 对象抽象而成的类，通常称作数据模型
class Word:
    eng = ""
    chn = ""

    def __init__(self, eng, chn):
        self.eng = eng
        self.chn = chn


# 英汉字典类，储存管理大量的词条，功能是通过英文，找出对应的中文
class Dictionary:
    # 通过列表，储存大量词条
    word_list = []

    # 字典创建出来就应该有词条
    def __init__(self):
        # 读取文件，获得词条字符串
        lines = self.read_file("中英文对照表.txt")
        # 解析lines中的每一个字符串，获得字符串中的信息，创建词条对象
        self.anazy_lines(lines)
        return

    def read_file(self, path):
        file = open(path, "r", encoding="utf-8")  # 读取文件
        lines = file.readlines()  # 读取每一行  readlines() 表示把文件的每一行当成一个字符串来读取，然后放在一个列表中
        return lines

    # 解析读取文件获得的字符串列表
    def anazy_lines(self, lines):
        for line in lines:
            # line就是每一行字符串，在这里进行解析，建模
            self.anazy_line(line)
        return

    # 解析一行数据，即一个词条数据
    def anazy_line(self, line):
        # a     pron.一个
        line_list = line.split("\t")
        # ['a', 'pron.一个']
        # 建模
        word = Word(line_list[0], line_list[1])  # line_list[0]即'a',Word为前面的一个类
        # 将词条装进列表
        self.word_list.append(word)
        return

    # 根据英文查找中文
    def find_chn_from_eng(self, eng):
        for word in self.word_list:
            if word.eng == eng:
                return self.repair_word(word.chn)
        return "查无此词，请检测您的输入，或期待本产品版本更新\n"

    # 修正中文 n. 发现;发现物\nv. 发现;找出 去掉两种释义中间的\n
    @staticmethod
    def repair_word(word):
        return word.replace("\\n", "\n")


# 1.使用字典
dictionary = Dictionary()

print("========================")
print("欢迎使用千锋老潘英汉词典")
print("========================")
while True:
    eng = input()
    print(dictionary.find_chn_from_eng(eng))
