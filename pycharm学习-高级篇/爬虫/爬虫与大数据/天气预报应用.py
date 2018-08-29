# -*- coding: utf-8 -*-
"""
Created on Tue May 15 22:53:39 2018
根据用户输入的城市，通过网络得到天气和温度
@author: yq
"""
import re
import urllib.request as r
#和程序可以进行交互，用户输入内容
city=input('请输入您要查询的城市名称(英文拼音)')
#print('http:'+city+'.com')
url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8','ignore')

wea=re.compile('"description":"(.*?)",').findall(data)
temp=re.compile('"temp_min":(.*?),').findall(data)
print("天气是：",wea)
print('温度是：',temp)

