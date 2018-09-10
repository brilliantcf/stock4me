# coding=utf-8
import tushare as ts
import stockstats

begin_time = '2017-02-01'
end_time = '2017-11-01'
code = "000001"
stock = ts.get_hist_data(code, start=begin_time, end=end_time)
stock["date"] = stock.index.values #增加日期列。
stock = stock.sort_index(0) # 将数据按照日期排序下。

stockStat = stockstats.StockDataFrame.retype(stock,code)
print(stockStat[['close','rsi_6','rsi_12']])

# begin_time = '2017-02-01'
# end_time = '2017-11-01'
# code = "000001"
# stock = ts.get_hist_data(code, start=begin_time, end=end_time)
# stock["date"] = stock.index.values #增加日期列。
# stock = stock.sort_index(0) # 将数据按照日期排序下。
#
# stockStat = stockstats.StockDataFrame.retype(stock,code)
# print(stockStat[['close','macd','macds','macdh']])




# begin_time = '2017-02-01'
# end_time = '2017-11-01'
# code = "000001"
# stock = ts.get_hist_data(code, start=begin_time, end=end_time)
# stock["date"] = stock.index.values #增加日期列。
# stock = stock.sort_index(0) # 将数据按照日期排序下。
#
# stockStat = stockstats.StockDataFrame.retype(stock,code)
# print(stockStat[['close','cci','cci_20']])

# begin_time = '2017-02-01'
# end_time = '2017-11-01'
# code = "000001"
# stock = ts.get_hist_data(code, start=begin_time, end=end_time)
# stock["date"] = stock.index.values #增加日期列。
# stock = stock.sort_index(0) # 将数据按照日期排序下。
#
# stockStat = stockstats.StockDataFrame.retype(stock,code)
# print(stockStat[['close','boll','boll_ub','boll_lb']])

# import matplotlib.pyplot as plt
# import tushare as ts
# import numpy as np
# import talib
#
# df=ts.get_k_data('600600')
# close = [float(x) for x in df['close']]
# # 调用talib计算指数移动平均线的值
# df['EMA12'] = talib.EMA(np.array(close), timeperiod=6)
# df['EMA26'] = talib.EMA(np.array(close), timeperiod=12)
#  # 调用talib计算MACD指标
# df['MACD'],df['MACDsignal'],df['MACDhist'] = talib.MACD(np.array(close),
#                             fastperiod=6, slowperiod=12, signalperiod=9)
# df.tail(12)
# print(df)