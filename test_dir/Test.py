# coding=utf-8
import os
import pandas as pd
import numpy as np
stdic=os.listdir(os.listdir(os.getcwd())[1])
del stdic[0]
date=['2012-07','2012-08']
#计算排序期J、持有期K内的对数收益率
def creturn(data,J,K):
    r=['','']
    r[0] = np.log(data[date[J-1]]['Adj Close'][0]/data[date[0]]['Adj Close'][-1])   #排序期收益率
    r[1] = np.log(data[date[J+K-1]]['Adj Close'][0]/data[date[J]]['Adj Close'][-1]) #持有期内收益率
    return r
rank=[]
#对每一个股票csv数据进行以上的计算并放入rank列表中
for item in stdic:
    fname = 'data/'+item
    data=pd.read_csv(fname)
    data=data.dropna()
    # data['Date'] = pd.to_datetime(data['Date'])
    # data = data[(data['Date'] >='20120701') & (data['Date'] <= '20120831')]
    data['Date'] = pd.to_datetime(data['Date'])
    data = data[(data['Date'] >= pd.to_datetime('20120701')) & (data['Date'] <= pd.to_datetime('20120831'))]
    data=data.set_index(['Date'])
    rank.append(creturn(data,1,1)[0])

