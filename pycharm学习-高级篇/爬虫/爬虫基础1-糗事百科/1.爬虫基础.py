'''爬取过程：
1.爬取网页
2.储存数据
3.预处理
  3.1提取文字
  3.2中午分词
  3.3消除噪音 (广告，导航条等等)
  3.4索引处理
  3.5链接关系的计算
  3.6特殊文件的处理
4.排名和检索

搜索引擎工作原理：
1.爬取网页
2.处理网页  提取关键词   建立索引库和索引
3.提供检索服务

http的请求方式：
get:url
post
put
delete
head
options
'''

# 1.读取网页  urllib.request.urlopen是打开某个网站的函数
import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")  # 向指定的url地址发起请求(这里是百度的网址)，并返回服务器响应的数据（文件对象）
data = response.read()  # 读取文件的全部内容
print(data)
print(type(data))
print(len(data))
print('\n')

# 读取一行
data = response.readline()  # 读取第一行(这里应该为空，因为百度网址第一行本来就是空的)
print('读取一行:', data)
print(type(data))
print(len(data))
print('\n')

# 读取全部
data = response.readlines()  # 读取全部的行,这点可以参考文件读取
print('读取全部:', data)
print(type(data))
print(len(data))
print('\n')

# for i in range(0, 100):
#     data = response.readline()
#     print(data)



# 2.爬取网页并保存html文件
response = urllib.request.urlopen("http://www.baidu.com")  # 向指定的url地址发起请求(这里是百度的网址)，并返回服务器响应的数据（文件对象）
data = response.read()  # 读取文件的全部内容，注意网页需要是html文件
with open(r"G:\day08\day08\ap.html", "wb") as f:  # "G:\day08\day08\app.txt"是文件路径;  wb：以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果文件不存在，则会自动创建一个文件。
    f.write(data)  # 写入文件地址

print(response.getcode())  # 返回状态码