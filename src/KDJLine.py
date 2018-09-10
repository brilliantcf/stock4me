# coding=utf-8
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
import json
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.stock
df=ts.get_hist_data('600800',start='2017-12-01',end='2017-12-31')
# db.temp.insert(json.loads(df.to_json(orient='records')))
df=df.sort_index()
df.index=pd.to_datetime(df.index,format='%Y-%m-%d')
#收市股价
close= df.close
highPrice=df.high
lowPrice=df.low
#每天的股价变动百分率
ret=df.p_change/100
 # 调用talib计算MACD指标
df['k'],df['d']=talib.STOCH(np.array(highPrice),np.array(lowPrice),np.array(close),
  fastk_period=9,slowk_period=3,slowk_matype=0,slowd_period=3,slowd_matype=0)

sig_k=df.k
print (type(sig_k))
sig_d=df.d
sig_j=df.k*3-df.d*2

# db.KDJ.insert(json.loads(df.to_json(orient='records')))
