# coding=utf-8
#
# date：日期
# open：开盘价
# high：最高价
# close：收盘价
# low：最低价
# volume：成交量
# price_change：价格变动
# p_change：涨跌幅
# ma5：5
# 日均价
# ma10：10
# 日均价
# ma20:20
# 日均价
# v_ma5:5
# 日均量
# v_ma10:10
# 日均量
# v_ma20:20
# 日均量
# turnover:换手率[注：指数无此项]


import tushare as ts
from pymongo import MongoClient
import json
import pandas as pd
import numpy as np


def getcodeList():
    client = MongoClient('mongodb://127.0.0.1:27017/')
    db = client.test
    stockCodeList = []
    for item in db.stockCode.find():
        # print item.get('SYMBOL')
        code = item.get('SYMBOL').encode('utf-8')
        if code not in stockCodeList:
            stockCodeList.append(code)
    return stockCodeList
# df = ts.get_profit_data(2017,3)
# db.historytradeInfo.insert(json.loads(df.to_json(orient='records')))

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.stock
codeList = getcodeList()

for code in codeList:
    if code == '' or code is None:
        continue
    else:
        df = ts.get_hist_data(code, start='2018-01-26', end='2018-01-26')
        try:
            df1 =df.reset_index()
        except Exception:
            print('NoneType object has no attribute reset_index')
        # print df
        if df1 is None:
            continue
        else:
            df1['code'] = code
            try:
                db.cftest.insert(json.loads(df1.to_json(orient='records')))
            except Exception:
                print(df1)
                print(df1['code'])

        # print type(df)
        # if df is not None :
        # df.dropna(axis=1)

        # db.historytradeInfo.insert(json.loads(df.to_json(orient='records')))
        # print df
        # if df is None:
        #     continue
        # else:
        #     # historytradeInfo_list =
        #     # if code not in db.historytradeInfo.find().batch_size(10):
        #         # print type(historytradeInfo_list)
        #         db.historytradeInfo.insert(json.loads(df.to_json(orient='records')))


# df = ts.get_tick_data('603238',date='2014-12-22')
# df['code']='600848'
# print df