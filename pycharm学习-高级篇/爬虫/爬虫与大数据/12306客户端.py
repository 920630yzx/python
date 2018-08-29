# -*- coding: utf-8 -*-
"""
Created on Tue May 29 21:27:59 2018

@author: yq
"""
from 抢票v1 import *
username,pwd,cardname,cardid,mobile=open('./login_users.txt','r').readline().split(",")
tickercontrol=TickerControl(LoginUser(username,pwd,cardname,cardid,mobile))




'1234'[:-1]
list('368')