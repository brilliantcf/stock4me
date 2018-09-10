from pymongo import MongoClient
import json
import tushare as ts
client = MongoClient('mongodb://localhost:27017/')
#df = ts.get_industry_classified()


def industry_classified():
    df = ts.get_industry_classified()
    db = client.test
    conn = db['industryclassified']
    conn.insert(json.loads(df.to_json(orient='records')))


def concept_classified():
    df = ts.get_concept_classified()
    db=client.test
    conn=db['conceptclassified']
    conn.insert(json.loads(df.to_json(orient='records')))

concept_classified()