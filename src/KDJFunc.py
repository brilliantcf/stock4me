#coding=utf-8
import tushare as ts
import talib as ta
import numpy as np
import pandas as pd
import os,time,sys,re,datetime
import csv
import scipy
import smtplib
from email.mime.text import MIMEText


def Get_Stock_List():
    df = ts.get_stock_basics()
    return df


# 按照MACD，KDJ等进行分析
def Get_TA(df_Code):
    operate_array2 = []
    count = 0
    for code in df_Code.index:
        df = ts.get_hist_data(code, start='2015-11-20')
        dflen = df.shape[0]
        count = count + 1
        if dflen>35:
            operate2 = Get_KDJ(df)
            operate_array2.append(operate2)
    df_Code['KDJ'] = pd.Series(operate_array2, index=df_Code.index)
    return df_Code


# 通过KDJ判断买入卖出
def Get_KDJ(df):
    # 参数9,3,3
    slowk, slowd = ta.STOCH(np.array(df['high']), np.array(df['low']), np.array(df['close']), fastk_period=9,
                            slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

    slowkMA5 = ta.MA(slowk, timeperiod=5, matype=0)
    slowkMA10 = ta.MA(slowk, timeperiod=10, matype=0)
    slowkMA20 = ta.MA(slowk, timeperiod=20, matype=0)
    slowdMA5 = ta.MA(slowd, timeperiod=5, matype=0)
    slowdMA10 = ta.MA(slowd, timeperiod=10, matype=0)
    slowdMA20 = ta.MA(slowd, timeperiod=20, matype=0)

    # 16-17 K,D
    df['slowk'] = pd.Series(slowk, index=df.index)  # K
    df['slowd'] = pd.Series(slowd, index=df.index)  # D
    dflen = df.shape[0]
    MAlen = len(slowkMA5)
    operate = 0
    # 1.K线是快速确认线——数值在90以上为超买，数值在10以下为超卖；D大于80时，行情呈现超买现象。D小于20时，行情呈现超卖现象。
    if df.iat[(dflen - 1), 16] >= 90:
        operate = operate - 3
    elif df.iat[(dflen - 1), 16] <= 10:
        operate = operate + 3

    if df.iat[(dflen - 1), 17] >= 80:
        operate = operate - 3
    elif df.iat[(dflen - 1), 17] <= 20:
        operate = operate + 3

    # 2.上涨趋势中，K值大于D值，K线向上突破D线时，为买进信号。#待修改
    if df.iat[(dflen - 1), 16] > df.iat[(dflen - 1), 17] and df.iat[(dflen - 2), 16] <= df.iat[(dflen - 2), 17]:
        operate = operate + 10
    # 下跌趋势中，K小于D，K线向下跌破D线时，为卖出信号。#待修改
    elif df.iat[(dflen - 1), 16] < df.iat[(dflen - 1), 17] and df.iat[(dflen - 2), 16] >= df.iat[(dflen - 2), 17]:
        operate = operate - 10

    # 3.当随机指标与股价出现背离时，一般为转势的信号。
    if df.iat[(dflen - 1), 7] >= df.iat[(dflen - 1), 8] and df.iat[(dflen - 1), 8] >= df.iat[(dflen - 1), 9]:  # K线上涨
        if (slowkMA5[MAlen - 1] <= slowkMA10[MAlen - 1] and slowkMA10[MAlen - 1] <= slowkMA20[MAlen - 1]) or \
                (slowdMA5[MAlen - 1] <= slowdMA10[MAlen - 1] and slowdMA10[MAlen - 1] <= slowdMA20[MAlen - 1]):  # K,D下降
            operate = operate - 1
    elif df.iat[(dflen - 1), 7] <= df.iat[(dflen - 1), 8] and df.iat[(dflen - 1), 8] <= df.iat[(dflen - 1), 9]:  # K线下降
        if (slowkMA5[MAlen - 1] >= slowkMA10[MAlen - 1] and slowkMA10[MAlen - 1] >= slowkMA20[MAlen - 1]) or \
                (slowdMA5[MAlen - 1] >= slowdMA10[MAlen - 1] and slowdMA10[MAlen - 1] >= slowdMA20[MAlen - 1]):  # K,D上涨
            operate = operate + 1

    return (df, operate)

dftemp= Get_Stock_List()
df = Get_TA(dftemp)
print(df)