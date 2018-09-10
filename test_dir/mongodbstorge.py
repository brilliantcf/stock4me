from pymongo import MongoClient
import json
import tushare as ts
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.test


news_codes =[]
for data in db.stockCode.find():
    data_codes = data.get('CODE')
    news_codes.append(data_codes)

for code in news_codes:
    codestr = code.encode("gbk")
        # print codestr[1:len(codestr)]
    df = ts.get_k_data(codestr[1:len(codestr)])
    if df is not None and isinstance(df, pd.DataFrame) and not df.empty:
        conn = db['mystock']
        conn.insert(json.loads(df.to_json(orient='records')))
    # print df
# client = MongoClient('mongodb://localhost:27017/')
# # conn = pymongo.Connection('127.0.0.1', port=27017)
# df = ts.get_tick_data('600848',date='2017-08-16')
#
# db = client.test
# conn = db['mystock']
# # client.db.tickdata.insert(json.loads(df.to_json(orient='records')))
