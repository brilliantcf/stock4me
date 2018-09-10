import tushare as ts
from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
df=ts.get_report_data(2017,1)
db = client.test
conn = db['stockachivement']
# client.db.tickdata.insert(json.loads(df.to_json(orient='records')))
conn.insert(json.loads(df.to_json(orient='records')))