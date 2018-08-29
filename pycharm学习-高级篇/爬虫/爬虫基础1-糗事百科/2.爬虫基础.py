# 爬取网页并保存
import urllib.request

urllib.request.urlretrieve("http://www.baidu.com", filename="G:/aa.html")  # "http://www.baidu.com"访问地址; 保存至"G:/aa.html"中，"G:/aa.html"也即是html文件路径
# urlretrieve   该方法在执行的过程中会产生缓存   因此需要清除,以防内存占满
urllib.request.urlcleanup()  # 清除缓存

