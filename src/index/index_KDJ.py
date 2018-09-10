# coding=utf-8

import baostock as bs
import pandas as pd
import numpy as np
import talib as ta
import datetime


stockcodelist =['sh.600137']

login_result =bs.login(user_id='anonymous', password='123456')
print('login respond error_msg:'+login_result.error_msg)

startdate = '2018-07-01'
today = datetime.datetime.now()
delta = datetime.timedelta(days=1)
# 获取截至上一个交易日的历史行情
predate = today - delta
# print(predate)
strpredate = datetime.datetime.strftime(predate, '%Y-%m-%d')
# print(strpredate)

for stockcode in stockcodelist:
    rs = bs.query_history_k_data("%s" % stockcode,"date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM",start_date=startdate, end_date=strpredate,
                                 frequency="d", adjustflag="2")
    print('query_history_k_data respond error_code:' + rs.error_code)
    print('query_history_k_data respond error_msg:' + rs.error_msg)

    result_list = []
    while (rs.error_code == '0') &rs.next():
        result_list.append(rs.get_row_data())
        result = pd.DataFrame(result_list, columns=rs.fields)
        # print(result)
        closelist = [float(price) for price in list(result['close'])]
        # print(closelist)
        highlist = [float(price) for price in list(result['high'])]
        # print(highlist)
        lowlist = [float(price) for price in list(result['low'])]
        # print(lowlist)


