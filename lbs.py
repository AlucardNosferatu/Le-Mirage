# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 17:30:32 2018

@author: Scrooge
"""
from urllib import *
import json

def lbs():
    head='http://api.map.baidu.com/location/ip?'
    ak='nChEZ2xDtmNtfi0ij59GOhjI3kDfGoKb'
    tail='ak='+ak+'&coor=bd09ll'
    rs = urlopen(head+tail)
    data = rs.read()
    address = json.loads(data)['content']['address_detail']['province']+json.loads(data)['content']['address_detail']['city']
    return address