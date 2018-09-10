# coding=utf-8

import talib as ta
import numpy as np
import pandas as pd
import tushare as ts
import datetime
import pymongo
import json

from sqlalchemy import false

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['test']

def getcodeList():
    stockCodeList = []
    for item in db.stockCode.find():
        code = item.get('SYMBOL').encode('utf-8')
        if code not in stockCodeList:
            stockCodeList.append(code)
    return stockCodeList


# 提取收盘价
def get_cci_by_stock_code(startdate,enddate,code):
    df = ts.get_k_data(code.decode('utf-8'), start=startdate, end=enddate)
    # print(df)
    if df.empty == False:
        # print(df)
        datearray = np.array(df['date'])
        codearray = np.array(df['code'])
        closed = df['close'].values
        upper, middle, lower = ta.BBANDS(closed, timeperiod=20,nbdevup=2,matype=0)
        df = pd.DataFrame([codearray, datearray, upper, middle, lower]).T
        df.columns = ['code', 'date', 'upper', 'middle', 'lower']
        print(df)
        if len(df)>0 :
            db.boll.insert(json.loads(df.T.to_json()).values())


startdate = '2018-06-01'
enddate='2018-08-17'
# today = datetime.datetime.now()
# delta = datetime.timedelta(days=1)
# # 获取截至上一个交易日的历史行情
# predate = today - delta
# print(predate)
# strpredate = datetime.datetime.strftime(predate, '%Y-%m-%d')
stock_list=getcodeList()
for code in stock_list:
    get_cci_by_stock_code(startdate,enddate,code)