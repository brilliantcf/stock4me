# -*- encoding:utf-8 -*-
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.stock


def getHighValue(stockcode):
    print stockcode


for item in db.stockCode.find():
    stockcode = item.get('SYMBOL').encode('utf-8')
    getHighValue(stockcode)
    # print type(stockCode)
    # averageH = getHighValue(stockcode)
    # averageL = getLowValue(stockcode)
    # print "stockCode" + stockcode + 'averageH:' + averageH + 'averageL:' + averageL

def getHighValue(stcode=None):
    print type(stcode)
    # code= stcode
    highTotal = 0;
    # if code is not None:
    for item in db.historytradeInfo.find({}).sort({"date": -1}).limit(10):
        high = item.get('high').encode('utf-8')
        highTotal = highTotal + high;
        averageHigh = highTotal / 10;
    return averageHigh

#
# def getHighValue(stcode=None):
#     print type(stcode)
#     # code= stcode
#     highTotal = 0;
#     # if code is not None:
#     for item in db.historytradeInfo.find({'code': stcode}).sort({"date": -1}).limit(10):
#         high = item.get('high').encode('utf-8')
#         highTotal = highTotal + high;
#         averageHigh = highTotal / 10;
#     return averageHigh
#
#
# def getLowValue(stcode=None):
#     # code=stcode
#     lowTotal = 0;
#     if stcode is not None:
#         for item in db.historytradeInfo.find({'code': stcode}).sort({"date": -1}).limit(10):
#         # for item in db.historytradeInfo.find({'code': stcode}):
#             low = item.get('high').encode('utf-8')
#             lowTotal = lowTotal + low;
#             averageLow = lowTotal / 10;
#     return averageLow



