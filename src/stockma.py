# -*- coding: UTF-8 -*-
import tushare as ts
import Series
import pandas as pd
import numpy as np
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.stock
# array = list(posts.find())#posts是我的collection
# type(array)
array =list(db.h_tmp.find())
stock_data = pd.DataFrame(array)
# del stock_data['_id']
initdata =stock_data.drop(['_id'],axis=1)
codedata =np.array(initdata['code'])
codelist =codedata.tolist()
# print initdata
for name,item in initdata.groupby('code'):
    # print name,item
    # print type(name)
    # print type(item)
    stock_data = item
    # print stock_data
    if stock_data is not None:
        Series.rolling(window=30, center=False).mean()
        # stock_data['MA_30'] = pd.rolling_mean(stock_data['close'], 30)
        # stock_data['MA_30']=stock_data['close'].rolling(30)
        print stock_data['MA_30']
        # ma_list = [30, 60] #分别计算30日、60日的移动平均线
        # for ma in ma_list:
        # stock_data['MA_' + str(ma)] = pd.rolling_mean(stock_data['close'], ma)
        #     stock_data['MA_' + str(ma)] = stock_data['close'].rolling(ma)
        #     print stock_data['MA_' + str(ma)]

# stock_data=pd.DataFrame(initdata,index=codelist)
# print stock_data
# stock_data.reindex(columns=codelist)
# print stock_data.index
# codelist = list(set(codelist))
# for codev in codelist:
#     # print codev
#     dftemp = stock_data[codev]
#     print dftemp

db.close
client.close()

#     print dftemp
    # print stock_data.ix[601886]
# print stock_data
# groupstock = stock_data.groupby(['code']).mean()

    # if stock_data.get_value['code'] ==codev:
    #     print codev
        # print stock_data[[codev]]


#
# stock_data.reset_index(drop=True)
# print stock_data.index
# for indexs in stock_data.index:
#     print indexs
#     print(stock_data.loc[indexs].values[0:-1])

# print type(codelist)
# print stock_data


# for item in stock_data.iterrows():
#     print item
# print type(stock_data)
# df =pd.DataFrame(stock_data,index=[stock_data['code']])
# print df

# print stock_data

# print type(array)
# dictBycode ={}
# xlist=[];
# for dict in array:
#     for (d, x) in dict.items():
#         # print "key:" + d + ",value:" + str(x)
#         if d=='code' and (x not in dictBycode):
#             # print x
#             if x not in xlist:
#                 # print type(dict.items)
#                 xlist.append(x)
#                 dfBycode = pd.DataFrame.from_dict(dict,orient='index')
#                 dictBycode[x]=dfBycode
# print xlist
# print len(xlist)
    # print type(item)
    # print item
# .encode('utf-8')
# print stock_data
# print array

# stock_data.sort_values('date', inplace=True)
# # 计算指数平滑移动平均线EMA
# for ma in ma_list:
#     stock_data['EMA_' + str(ma)] = pd.ewma(stock_data['close'], span=ma)

# 将数据按照交易日期从近到远排序
# stock_data.sort('date', ascending=False, inplace=True)

