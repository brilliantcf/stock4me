import tushare as ts
import json
import pandas as pd
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.test

#get all stock codes
news_codes =[]
for data in db.stockCode.find():
    data_codes = data.get('CODE')
    news_codes.append(data_codes)

#get sum of close for each code
# thirtydayclose

# code30LineList =
for code in news_codes:
    codestr =code.encode("gbk")
    # print codestr[1:len(codestr)]
    df= ts.get_hist_data(codestr[1:len(codestr)], ktype='M',start='2017-08-18',end='2017-08-18')
    print codestr[1:len(codestr)]
    print type(codestr[1:len(codestr)])
    df['CODE']=codestr[1:len(codestr)]
    # print df
    # print type(df)
    if df is not None and isinstance(df, pd.DataFrame) and not df.empty:
        conn = db['ma30']
        conn.insert_many(json.loads(df.to_json(orient='records')))
