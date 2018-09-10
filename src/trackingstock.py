# -*- coding: UTF-8 -*-
import tushare as ts
from pymongo import MongoClient
import json
import pandas as pd
import numpy as np


def getcodeList():
    client = MongoClient('mongodb://192.168.146.187:27017/')
    db = client.test8
    stockCodeList = []
    for item in db.stockCode.find():
        # print item.get('SYMBOL')
        code = item.get('SYMBOL').encode('utf-8')
        if code not in stockCodeList:
            stockCodeList.append(code)
    return stockCodeList

client = MongoClient('mongodb://192.168.146.187:27017/')
db = client.test8
for item in db.scpool_33.find():
    print (type(item))