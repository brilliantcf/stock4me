# coding=utf-8

import talib as ta
import numpy as np
import pandas as pd

#通过RSI判断买入卖出
def Get_RSI(df):
    slowreal = ta.RSI(np.array(df['close']), timeperiod=14)
    fastreal = ta.RSI(np.array(df['close']), timeperiod=5)

    slowrealMA5 = ta.MA(slowreal, timeperiod=5, matype=0)
    slowrealMA10 = ta.MA(slowreal, timeperiod=10, matype=0)
    slowrealMA20 = ta.MA(slowreal, timeperiod=20, matype=0)
    fastrealMA5 = ta.MA(fastreal, timeperiod=5, matype=0)
    fastrealMA10 = ta.MA(fastreal, timeperiod=10, matype=0)
    fastrealMA20 = ta.MA(fastreal, timeperiod=20, matype=0)
    # 18-19 慢速real，快速real
    df['slowreal'] = pd.Series(slowreal, index=df.index)  # 慢速real 18
    df['fastreal'] = pd.Series(fastreal, index=df.index)  # 快速real 19
    dflen = df.shape[0]
    MAlen = len(slowrealMA5)
    operate = 0
    # RSI>80为超买区，RSI<20为超卖区
    if df.iat[(dflen - 1), 18] > 80 or df.iat[(dflen - 1), 19] > 80:
        operate = operate - 2
    elif df.iat[(dflen - 1), 18] < 20 or df.iat[(dflen - 1), 19] < 20:
        operate = operate + 2

    # RSI上穿50分界线为买入信号，下破50分界线为卖出信号
    if (df.iat[(dflen - 2), 18] <= 50 and df.iat[(dflen - 1), 18] > 50) or (
            df.iat[(dflen - 2), 19] <= 50 and df.iat[(dflen - 1), 19] > 50):
        operate = operate + 4
    elif (df.iat[(dflen - 2), 18] >= 50 and df.iat[(dflen - 1), 18] < 50) or (
            df.iat[(dflen - 2), 19] >= 50 and df.iat[(dflen - 1), 19] < 50):
        operate = operate - 4

    # RSI掉头向下为卖出讯号，RSI掉头向上为买入信号
    if df.iat[(dflen - 1), 7] >= df.iat[(dflen - 1), 8] and df.iat[(dflen - 1), 8] >= df.iat[(dflen - 1), 9]:  # K线上涨
        if (slowrealMA5[MAlen - 1] <= slowrealMA10[MAlen - 1] and slowrealMA10[MAlen - 1] <= slowrealMA20[MAlen - 1]) or \
                (fastrealMA5[MAlen - 1] <= fastrealMA10[MAlen - 1] and fastrealMA10[MAlen - 1] <= fastrealMA20[
                        MAlen - 1]):  # RSI下降
            operate = operate - 1
    elif df.iat[(dflen - 1), 7] <= df.iat[(dflen - 1), 8] and df.iat[(dflen - 1), 8] <= df.iat[(dflen - 1), 9]:  # K线下降
        if (slowrealMA5[MAlen - 1] >= slowrealMA10[MAlen - 1] and slowrealMA10[MAlen - 1] >= slowrealMA20[MAlen - 1]) or \
                (fastrealMA5[MAlen - 1] >= fastrealMA10[MAlen - 1] and fastrealMA10[MAlen - 1] >= fastrealMA20[
                        MAlen - 1]):  # RSI上涨
            operate = operate + 1

    # 慢速线与快速线比较观察，若两线同向上，升势较强；若两线同向下，跌势较强；若快速线上穿慢速线为买入信号；若快速线下穿慢速线为卖出信号
    if df.iat[(dflen - 1), 19] > df.iat[(dflen - 1), 18] and df.iat[(dflen - 2), 19] <= df.iat[(dflen - 2), 18]:
        operate = operate + 10
    elif df.iat[(dflen - 1), 19] < df.iat[(dflen - 1), 18] and df.iat[(dflen - 2), 19] >= df.iat[(dflen - 2), 18]:
        operate = operate - 10
    return (df, operate)

