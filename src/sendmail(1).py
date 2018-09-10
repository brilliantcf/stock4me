# coding=utf-8
import smtplib

import tushare as ts
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import datetime
import numpy as np
from pymongo import MongoClient
client = MongoClient('mongodb://192.168.151.111:27017/')
db = client.test8


from_addr='cf_maple@126.com'
password='1q2w!Q@W'
to_addr='stmonitor888@126.com'
smtp_server='smtp.126.com'

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),\
                       addr.encode('utf-8') if isinstance(addr,unicode) else addr))

def remind():
    for stock in db.scpool.find():
        code = stock["CODE"][1:]
        print code
        df = ts.get_realtime_quotes(code)
        open = float(df.ix[0, ['open']].values[0].encode('utf-8'))
        price = float(df.ix[0, ['price']].values[0].encode('utf-8'))

        if ((price - open) / open > 0.01):
            msg = MIMEText(df.ix[0, ['name']].values[0].encode('utf-8') + \
                           '实时价格' + str(price) + ',高于开盘价价：' + \
                           str(open), \
                           'plain', 'utf-8')
            msg['From'] = _format_addr(u'发革<%s>' % from_addr)
            msg['To'] = _format_addr(u'接收员<%s>' % to_addr)
            msg['Subject'] = Header(u'来自SMTP', 'utf-8')

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()







remind()