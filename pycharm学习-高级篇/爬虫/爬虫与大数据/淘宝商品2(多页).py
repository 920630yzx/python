# -*- coding: utf-8 -*-
"""
Created on Thu May 24 22:02:35 2018

@author: yq
"""

import urllib.request as r
import re
import pymysql
import pandas
conn=pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8')
#use test
#create table goods(tbtitle varchar(30),price varchar(10),ratetotal varchar(10),tbcontent varchar())
#insert into goods(tbtitle,price,ratetotal,tbcontent) values();
#一个函数，通过url,和参数，获得网页数据
utod=lambda url,q:r.urlopen(url).read().decode('utf-8','ignore')
utod2=lambda url,q:r.urlopen(url.format(q)).read().decode('utf-8','ignore')
utod3=lambda url,q:r.urlopen(url.format(q)).read().decode('gbk','ignore')

url='https://s.taobao.com/search?q=only&s={}&ajax=true'
for page in range(1,10):
    data=utod2(url,(page-1)*44)#str to json
    import json      #字典{}      字典    字典     数组[]
    itemlist=json.loads(data)['mods']['itemlist']['data']['auctions']
    #    字典{}
    for item in itemlist:
        print('第{}页\t商品名是：{}\t价格是：{}'.format(page,item['title'],item['view_price']))
        totalurl='https://dsr-rate.tmall.com/list_dsr_info.htm?itemId={}'
        itemid=re.compile('item.htm[?]id=(.*?)&').findall(item['detail_url'])[0]
        ratetotal=re.compile('"rateTotal":(.*?)}').findall(utod2(totalurl,itemid))[0]
        print("评价是：",ratetotal)
        descrcontenturl='https://detail.tmall.com/item.htm?id={}'
        content=re.compile('<meta name="description" content="(.*?)"/>').findall(utod3(descrcontenturl,itemid))[0]
        print("商品描述是：",content)
        insertsql='insert into goods(tbtitle,price,ratetotal,tbcontent) values("{}","{}","{}","{}")'
        pandas.read_sql(insertsql.format(item['title'][0:29],item['view_price'],ratetotal,'todo.'),conn)
        
        
        
        