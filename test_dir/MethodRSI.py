# coding=utf-8
import talib
import numpy as np
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.test

def initialize(context):
    # 定义一个全局变量, 保存要操作的证券
    # context.stocks =
    context.LOW_RSI = 30
    context.HIGH_RSI = 70
    # # 设置我们要操作的股票池
    # set_universe(context.stocks)

def get_prices():

    for codes in db.stockCode.find():
        profitUrl = codes.get('')

# 初始化此策略
def handle_data(context, data):
    # 取得当前的现金
    cash = context.portfolio.cash
    # 循环股票列表
    for stock in context.stocks:
        # 获取股票的收盘价数据,talib参数取14，前14天的rsi无法计算，所以取15天的数据
        # prices = attribute_history(stock, 15, '1d', ('close'))
        # 创建RSI买卖信号，包括参数timeperiod
        # 注意：RSI函数使用的price必须是narray
        rsi = talib.RSI(prices['close'].values, timeperiod=14)[-1]
        # 获取当前股票的数据
        current_position = context.portfolio.positions[stock].amount
        # 获取当前股票价格
        current_price = data[stock].price
        # 当RSI信号小于30，且拥有的股票数量大于0时，卖出所有股票
        if rsi < context.LOW_RSI and current_position > 0:
            order_target(stock, 0)
        # 当RSI信号大于70, 且拥有的股票数量为0时，则全仓买入
        elif rsi > context.HIGH_RSI and current_position == 0:
            number_of_shares = int(cash/current_price)
            # 购买量大于0时，下单
            if number_of_shares > 0:
                # 买入股票
                order(stock, +number_of_shares)
                # 记录这次买入
                log.info("Buying %s" % (stock))
