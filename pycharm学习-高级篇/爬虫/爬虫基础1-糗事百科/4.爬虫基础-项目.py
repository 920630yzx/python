# 项目：爬取糗事百科的一些数据(https://www.qiushibaike.com/)
import urllib.request
import re  # 导入正则


def jokeCrawler(url):
    # 1.定义请求头：  {}括号里是一个常用请求头,固定写法；Mozilla/5.0表示火狐浏览器5.0版本
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"}
    # 2.发送请求：     urllib.request.Request()函数
    req = urllib.request.Request(url, headers=headers)
    # 3.获取响应：     urllib.request.urlopen()函数
    response = urllib.request.urlopen(req)
    # 4.读取数据，按照uft-8编码格式进行数据的获取,防止乱码      # response.read()读取文件的全部内容
    HTML = response.read().decode("utf-8")

    # 5.正则主体部分：   (前后匹配)    \表示换行，pat有两种写法，参见下面：
    pat = r'<div class="author clearfix">(.*?)' \                
          r'<span class="stats-vote"><i class="number">'

    # pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)  # 正则匹配,爬取数据；re.S是一个正则的规则

    divsList = re_joke.findall(HTML)  # 查找所有的信息
    print(divsList)  # 打印信息


    dic = {}   # 定义一个字典
    for div in divsList:  # 遍历所有页面的数据

        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)  # 这里re.compile是正则匹配与前者一样  (得到用户名)
        userName = re_u.findall(div)  # 得到所有的用户名   findall是查找所有符合匹配的字段
        print(userName)
        userName = userName[0]  # 获取第一个元素

        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)  #re.S表示多行匹配  # re.compile正则匹配,爬取数据   \n表示换行   #不要r好像也行
        duanzi = re_d.findall(div)  # 得到爬取内容
        duanzi = duanzi[0]  # 获取第一个元素

        dic[userName] = duanzi  # 将所有的数据存储到字典中
    return dic

url = "https://www.qiushibaike.com/text/page/4/"  # 网站
info = jokeCrawler(url)  # 调用函数

for k,v in info.items():   # 键值对字典遍历
    print(k+"\n说"+v)






































