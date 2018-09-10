# coding=utf-8
import tushare as ts
df = ts.get_hist_data("600848", start='2017-01-01', end='2017-12-08')
# print df
print df.reset_index()
# print df.get("date")
# print type(df.index)
# print df.set_index('date')
# print df.index