# encoding: utf-8
import pandas as pd
import datetime
import tushare as ts
# print ts.get_hist_data('600848', ktype='M') #获取月k线数据
# print type(ts.get_hist_data('600848', ktype='M'))
# date = datetime.datetime.now()
# date_from = datetime.datetime(date.year, date.month, date.day)
# print date_from.strftime("%Y-%m-%d")
df =ts.get_hist_data('600848', ktype='M',start='2017-08-18',end='2017-08-18')
df['CODE']="808909"
print  df
# return date_from
# stock_data = pd.read_csv(r'000300.csv', parse_dates=[1],encoding='gb2312')
# print (stock_data)
# print stock_data
# stock_data.head()
# stock_data.sort('日期', inplace=True)
# stock_data.head()
# ma=30
# stock_data['ma_'+str(ma)]=pd.rolling_mean(stock_data['收盘价'],ma)
# stock_data.to_csv('000300_ma.csv',index=False)
