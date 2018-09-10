import tushare as ts
from pymongo import MongoClient
import json
#
# client = MongoClient('mongodb://127.0.0.1:27017/')
# db = client.stock
# df = ts.get_stock_basics()
# # db.profitability.insert(df.to_dict())
# # print type(ts.get_profit_data(2017,3))
#
# db.stockbasics.insert(json.loads(df.to_json(orient='records')))

datas =ts.get_hist_data('600848',start='2008-01-01',end='2018-01-01')
print datas