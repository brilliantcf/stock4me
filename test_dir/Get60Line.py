import tushare as ts
import json
import pandas as pd
from pandas import Series,DataFrame
import pymongo
from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client.test


stockInfoDataframe = pd.DataFrame(list(db.stock.find()))
# print stockInfoDataframe.nlargest(10,columns='TIME')
# print Series.rolling(window=60,center=False).mean()
stock_data['ma_'+str(20)]=pd.rolling_mean(stock_data['收盘价'],20)
