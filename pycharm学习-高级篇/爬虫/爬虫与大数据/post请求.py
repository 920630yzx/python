# -*- coding: utf-8 -*-
"""
Created on Thu May 17 21:29:52 2018

@author: yq
"""
url = "http://www.iqianyue.com/mypost/"
import urllib.request as r
#参数，name,pass
"""
name: qqyu
pass: 123
"""
req=r.Request(url,'name=qqyu&pass=123'.encode())
data=r.urlopen(req).read().decode('utf-8','ignore')
print(data)




