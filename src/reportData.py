# coding=utf-8
# 网易大盘历史数据
import os
import csv
import pymongo
import re
import numpy as np
# 日期
# 股票代码
# 名称
# 收盘价
# 最高价
# 最低价
# 开盘价
# 前收盘
# 涨跌额
# 涨跌幅
# 成交量
# 成交金额

class c_stock:
    def __init__(self,date, code, close,high,low, open,pre_close ,value_change,p_change,volume,amount):
            self.date = date
            self.code = code
            # self.name = name
            self.close = close
            self.high = high
            self.low = low
            self.open = open
            self.pre_close = pre_close
            self.value_change = value_change
            self.p_change = p_change
            self.volume = volume
            self.amount = amount
            # print 'date' + date + 'code' + code + 'name' + name + 'close' + close + 'high' + high + 'low' + low + 'open' + open + 'pre_close' + pre_close + 'value_change' + value_change + 'p_change' + p_change + 'volume' + volume + 'amount' + amount;


#mongodb_link = 'mongodb://127.0.0.1:27017'
#mongoClient = MongoClient(mongodb_link)
# client = MongoClient('mongodb://192.168.135.173:27017/')
# db = client.test
conn = pymongo.MongoClient("192.168.146.102", 27017)
# conn.db_stock.authenticate("d","zz")
db = conn.test8

def write_dict(type):
    db.maketInfos.insert(type.__dict__)


#db.stocks.drop()
#db.stocks.remove({})
reader = csv.reader(file('000001.csv','rb'))
for row in reader:
    if reader.line_num == 1:
        continue
    # print 'date' + row[0] + 'name' + row[2] + 'close' + row[3] + 'high' + row[4] + 'low' + row[5] + 'open' + row[
    #     6] + 'pre_close' + row[7] + 'value_change' + row[8] + 'p_change' + row[9] + 'volume' + row[10] + 'amount' + row[
    #           11];
    one = c_stock(code='000001',
                      date=row[0],
                      # name=(row[2]).decode("unicode_escape"),
                      close=float(row[3]),
                      high=float(row[4]),
                      low=float(row[5]),
                      open =float(row[6]),
                    pre_close=float(row[7]),
                  value_change=float(row[8]),
                  p_change=float(row[9]),
                  volume=float(row[10]),
                  amount =float(row[11]))
    write_dict(one)

print db.maketInfos.count()
#time.sleep(3)
#for i in db.stocks.find():
#    print i