# coding=utf-8
# code,代码
# name,名称
# roe,净资产收益率(%)
# net_profit_ratio,净利率(%)
# gross_profit_rate,毛利率(%)
# net_profits,净利润(万元)
# esp,每股收益
# business_income,营业收入(百万元)
# bips,每股主营业务收入(元)

import tushare as ts
from pymongo import MongoClient
import json

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.stock

# if db.stockCode.count() != 0:
#     # if db.profitabilityInfo.count()
#     news_codes = []
#     for data in db.stockCode.find():
#         data_codes = data.get('CODE')
#         news_codes.append(data_codes)
#     for item in news_codes:
#         ts.
df = ts.get_profit_data(2017,3)
# db.profitability.insert(df.to_dict())
# print type(ts.get_profit_data(2017,3))

db.profitability.insert(json.loads(df.to_json(orient='records')))