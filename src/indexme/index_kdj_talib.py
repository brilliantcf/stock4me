# coding=utf-8

import talib as ta
import numpy as np
import pandas as pd
import tushare as ts
import datetime
import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['test']

def lm_kdj():
    # df = ts.get_k_data(code.decode('utf-8'), start=startdate, end=enddate)
    df = ts.get_k_data('600600')
    df = df[300:]
    df.index = range(len(df))
    if df.empty == False:
        # df.index = range(len(df))
        datearray = np.array(df['date'])
        codearray = np.array(df['code'])
        df['slowk'], df['slowd'] = ta.STOCH(df['high'].values,
                                            df['low'].values,
                                            df['close'].values,
                                            fastk_period=9,
                                            slowk_period=3,
                                            slowk_matype=0,
                                            slowd_period=3,
                                            slowd_matype=0)
        df['slowj'] = 3.0 * df['slowk'] - 2.0 * df['slowd']
        # print df['slowk'], df['slowd']
        # print df['slowj']
        dfT = pd.DataFrame([codearray, datearray, df['slowk'], df['slowd'], df['slowj']]).T
        dfT.columns = ['code', 'date', 'slowk', 'slowd', 'slowj']
        if len(df)>0 :
            db.kdj.insert(json.loads(dfT.T.to_json()).values())

def getcodeList():
    stockCodeList = []
    for item in db.stockCode.find():
        code = item.get('SYMBOL').encode('utf-8')
        if code not in stockCodeList:
            stockCodeList.append(code)
    return stockCodeList

# startdate = '2017-06-01'
# enddate='2018-08-22'
# today = datetime.datetime.now()
# delta = datetime.timedelta(days=1)
# # 获取截至上一个交易日的历史行情
# predate = today - delta
# print(predate)
# strpredate = datetime.datetime.strftime(predate, '%Y-%m-%d')
# stock_list=getcodeList()
# for code in stock_list:
#     lm_kdj(startdate,enddate,code)
lm_kdj()