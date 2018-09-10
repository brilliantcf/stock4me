# coding=utf-8
# tushare 获取大盘数据

import tushare as ts
from pymongo import MongoClient
import json


client = MongoClient('mongodb://192.168.135.173:27017/')
db = client.test
maketdata=ts.get_index()
db.cftest.drop()
db.cftest.insert(json.loads(maketdata.to_json(orient='records')))

