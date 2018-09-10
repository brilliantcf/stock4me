import tushare as ts
import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['test']
df =ts.get_stock_basics()
db.stockbasics.insert(json.loads(df.to_json(orient='records')))

