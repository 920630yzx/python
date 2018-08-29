from lxml import etree
import requests
import json

# 获取要抓取的网页地址
url = 'https://www.qiushibaike.com/'

response = requests.get(url=url)
response.encoding = 'utf-8'

# print(response.text)

tree = etree.HTML(response.text)
print(tree)

name_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/h2/text()')   # 获取所有的用户名
for name in name_list:
	print(name)



src_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/img/@src')  # 获取所有图片的地址
for src in src_list:
	print(src)



autor_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]')
items = []
for autor in autor_list:
	item = {                                      # for autor in autor_list:
		'name':autor.xpath('./a/h2/text()'),      # 继续遍历查找  'name':autor.xpath('./a/h2/text()')分别是键值对和对应的值
		'src':autor.xpath('./a/img/@src')         # 继续遍历查找   src = autor.xpath('./a/img/@src')
	}
	items.append(item)

print(items)

json_str = json.dumps(items)  # 字典中的单引号转换成双引号
print(json_str)
with open('items.json', 'w') as fp:  # 创建一个'items.json'并写入结果,可以看见一个名为items.json的文件
	fp.write(json_str)

# name_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/h2/text()')
# src_list = tree.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/img/@src')




'''# 使用xpath定位必须要使用的依赖库
from lxml import etree

# 读取本地的html文件
tree = etree.parse('1.html')

# 读取网络的html文件
# tree = etree.HTML('请求到的网页源码')

# print(tree)

# 查找所有的li标签
li_list = tree.xpath('//li')

print(li_list)

# 查找所有li标签的内容
content_list = tree.xpath('//li/text()')
print(content_list)

# 查找唐伯虎的诗
tbh_list = tree.xpath('//body/li/text()')
print(tbh_list)

# 只查找名言警句
statement_list = tree.xpath('//body/ul/li/text()')
print('----------------------')
print(statement_list)

# 查找所有包含class属性li标签的id属性内容
id_list = tree.xpath('//li[@class]/@id')
print(id_list)'''