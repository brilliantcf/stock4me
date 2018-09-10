# coding=utf-8

import tushare as ts
from pymongo import MongoClient
import datetime


#获取当天的前一天
def get_beforday():
    date=datetime.datetime.now()
    oneday = datetime.timedelta(days=1)
    day = date - oneday
    date_from = datetime.datetime(day.year, day.month, day.day)
    frm = date_from.strftime("%Y-%m-%d")
    return frm


# client = MongoClient('mongodb://127.0.0.1:27017/')
# db = client.stock

# df = ts.get_hist_data('603589', start='2017-12-11', end='2017-12-12')
# df = ts.get_hist_data('603589', start='2017-12-11', end='2017-12-11')
# print df
# codeList = historytradeInfo.getcodeList()
# for item in codeList:
#     df = ts.get_hist_data(item, start='2017-01-01', end='2017-12-08')
