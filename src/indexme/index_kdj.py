# coding=utf-8

import talib as ta
import tushare as ts
import numpy as np
import pandas as pd

#通过KDJ判断买入卖出
def Get_KDJ():
    df = ts.get_k_data('600600')
    slowk, slowd = ta.STOCH(np.array(df['high']), np.array(df['low']), np.array(df['close']), fastk_period=9,
                            slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    print(slowd,slowk)
    # slowkMA5 = ta.MA(slowk, timeperiod=5, matype=0)
    # slowkMA10 = ta.MA(slowk, timeperiod=10, matype=0)
    # slowkMA20 = ta.MA(slowk, timeperiod=20, matype=0)
    # slowdMA5 = ta.MA(slowd, timeperiod=5, matype=0)
    # slowdMA10 = ta.MA(slowd, timeperiod=10, matype=0)
    # slowdMA20 = ta.MA(slowd, timeperiod=20, matype=0)

    # 16-17 K,D
    # df['slowk'] = pd.Series(slowk, index=df.index)  # K
    # print(df['slowk'])
    # df['slowd'] = pd.Series(slowd, index=df.index)  # D
    # print(df['slowd'])
    dflen = df.shape[0]
    # MAlen = len(slowkMA5)
    operate = 0

Get_KDJ()