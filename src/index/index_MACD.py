# coding=utf-8
import tushare as ts
import stockstats
import pymongo
import json
import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient['test']

def getcodeList():
    stockCodeList = []
    for item in db.stockCode.find():
        # print item.get('SYMBOL')
        code = item.get('SYMBOL').encode('utf-8')
        if code not in stockCodeList:
            stockCodeList.append(code)
    return stockCodeList

def get_macd_by_stock_code(begin_time,end_time,stock_code):
    code_str=str(stock_code,'utf-8')
    stock = ts.get_hist_data(code_str, start=begin_time, end=end_time)
    if stock is None:
        print()
    else:
        stock["datep"] = stock.index.values #增加日期列。
        stock = stock.sort_index(0) # 将数据按照日期排序下。
        stock['stockcode']=code_str
        stockStat = stockstats.StockDataFrame.retype(stock,code_str)
        if len(stockStat)>0:
            df1 = stockStat[['stockcode','close','macd','macds','macdh','datep']]
            db.macd.insert(json.loads(df1.T.to_json()).values())

startdate = '1990-12-19'
today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
predate = today - delta
strpredate = datetime.datetime.strftime(predate, '%Y-%m-%d')
stock_list=getcodeList()
for code in stock_list:
    get_macd_by_stock_code(startdate,strpredate,code)