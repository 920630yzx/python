import urllib.request

#如果网页长时间响应，徐通需要判断是否超时（自己定），无法爬取数据
for i in range(1, 10):
    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.5)  # urllib.request.urlopen是打开网站的函数；timeout=0.5表示超过0.5秒就会报错
        print(len(response.read().decode("uft-8")))  # decode("uft-8")按照uft-8编码格式进行数据的获取(爬取的网页中有中文如果不是utf8格式，就会显示乱码)
    except:
        print("请求超时，继续爬取下一个内容")

