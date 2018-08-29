# -*- coding: utf-8 -*-
"""
Created on Thu May 24 20:47:03 2018

精简地址：
https://s.taobao.com/search?q=only&s=0&ajax=true          只有32条
https://s.taobao.com/search?q=only&s=44&ajax=true          44条
https://s.taobao.com/search?q=only&s=88&ajax=true          44条
总结规律：ajax=true是加载动态json数据，ajax=false加载网页数据.
页码的规则：(page-1)*44

注意点：如果查询的是带中文的需要转移为url识别的字符
https://s.taobao.com/search?q=裙子&s=0&ajax=true
https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&s=0&ajax=true
r.quote('裙子')#'%E8%A3%99%E5%AD%90'


需要获得的数据：
商品名：
价格：
detail_url:"//detail.tmall.com/item.htm?id=564744919280&ns=1&abbucket=4"
@author: yq
"""
import urllib.request as r
url='https://s.taobao.com/search?q=only&s=0&ajax=true'
#一个函数，通过url,和参数，获得网页数据
utod=lambda url,q:r.urlopen(url).read().decode('utf-8','ignore')
utod2=lambda url,q:r.urlopen(url.format(q)).read().decode('utf-8','ignore')
utod3=lambda url,q:r.urlopen(url.format(q)).read().decode('gbk','ignore')


data=utod(url,'')#str to json
import json      #字典{}      字典    字典     数组[]
itemlist=json.loads(data)['mods']['itemlist']['data']['auctions']
#    字典{}
for item in itemlist:
    print('商品名是：{}\t价格是：{}'.format(item['title'],item['view_price']))
    print('--',item['detail_url'])
    import re
    totalurl='https://dsr-rate.tmall.com/list_dsr_info.htm?itemId={}'
    itemid=re.compile('item.htm[?]id=(.*?)&').findall(item['detail_url'])[0]
    ratetotal=re.compile('"rateTotal":(.*?)}').findall(utod2(totalurl,itemid))
    print("评价是：",ratetotal)
    descrcontenturl='https://detail.tmall.com/item.htm?id={}'
    content=re.compile('<meta name="description" content="(.*?)"/>').findall(utod3(descrcontenturl,itemid))[0]
    print("商品描述是：",content)
    
"""
精简评价地址：
https://dsr-rate.tmall.com/list_dsr_info.htm?itemId=565269274119
({"dsr":{"itemId":0,"sellerId":0,"totalSoldQuantity":0,"spuId":0,"peopleNum":0,
"gradeAvg":4.8,"periodSoldQuantity":0,"rateTotal":228}})
商品描述地址：

<meta name="description" content=""/>

"""










