# coding=utf-8

import tushare as ts
import pymongo
import json
import datetime
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['test']

def get_3_by_pe(date):
    # print date
    df = ts.get_stock_basics(date)
    dft =df.sort_values(by=['pe'] ,ascending=True)
    df3=dft[0:3]
    return df3

def dateRange(beginDate, endDate): #获取时间List
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def get_3_by_pb():
    # print date
    df = ts.get_today_all()
    dft = df.sort_values(by=['pb'], ascending=True)
    df3 = dft[0:3]
    # df['pb_percent']=df['pb'].map(lambda x:x+100)
    print df3

def get_3_by_mktcap():
    df = ts.get_today_all()
    dft = df.sort_values(by=['mktcap'], ascending=True)
    df3 = dft[0:10]
    # df['pb_percent']=df['pb'].map(lambda x:x+100)
    print df3

get_3_by_mktcap()
# def per_stock_pool():
#     for date in dateRange('2018-01-01', '2018-01-20'):
#         print get_3_by_pe(date)
        # print df3

# per_stock_pool()

# db.closeDB()
#
# bs.query_history_k_data()
# def get_allprofit():
#     year = datetime.datetime.now().year
#     ts.get_profit_data(year, 3)
#     db.per.insert(json.loads(df.T.to_json()).values())
