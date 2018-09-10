# coding=utf-8
# 概念分类
import tushare as ts
from pymongo import MongoClient
import json

# E:\workspace\workspace_pycharmProjects\stock\src\conceptClassified.py
client = MongoClient('mongodb://192.168.135.173:27017/')
db = client.test8
conceptClassifieddata=ts.get_concept_classified()
db.conceptClassified.drop()
db.conceptClassified.insert(json.loads(conceptClassifieddata.to_json(orient='records')))