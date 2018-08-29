# -*- coding: utf-8 -*-
"""
Created on Thu May 10 22:26:03 2018
目标-百度
任务-
下载百度互联网网页内容
数据筛选(正则表达式)
保存
https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=python&rsv_spt=1&oq=python&rsv_pq=b7565cd30000c303&rsv_t=de8eSbwm22IzOJtsCbp1bpi%2BmwJNEzPREKTZvjo8%2F1R3fRMbR1LKdyO4bRy7M4CLryog&rqlang=cn&rsv_enter=0&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug4=910
@author: yq
"""
import re#Regular正则
import urllib.request as r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=baiduhome_pg&wd=python&rsv_spt=1&oq=python&rsv_pq=b7565cd30000c303&rsv_t=de8eSbwm22IzOJtsCbp1bpi%2BmwJNEzPREKTZvjo8%2F1R3fRMbR1LKdyO4bRy7M4CLryog&rqlang=cn&rsv_enter=0&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_sug4=910'
r.urlretrieve(url,filename='./baidu.html')


baidu=r.urlopen(url).read().decode('utf-8','ignore')
print(baidu)


re.compile('{"title":"(.*?)",',re.S).findall(baidu)














