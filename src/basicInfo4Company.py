# coding=utf-8

import tushare as ts
from pymongo import MongoClient
import json


client = MongoClient('mongodb://192.168.135.173:27017/')
db = client.test
maketdata=ts.get_stock_basics()
db.companyBasic.drop()
db.companyBasic.insert(json.loads(maketdata.to_json(orient='records')))