# coding=utf-8
import smtplib

import tushare as ts
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import datetime




from_addr='brilliantcf@126.com'
password='1q2w!Q@W'
to_addr='727435849@qq.com'
smtp_server='smtp.126.com'

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),\
                       addr.encode('utf-8') if isinstance(addr,unicode) else addr))

def remind():
    result=ts.get_today_all()
    for index, row in result.iterrows():
        if row.changepercent>=1:
            msg = MIMEText(row.name + row.code+datetime.datetime.now())
            msg['From'] = _format_addr(u'慧用科技<%s>' % from_addr)
            msg['To'] = _format_addr(u'接收员<%s>' % to_addr)
            msg['Subject'] = Header(u'来自SMTP', 'utf-8')

            server = smtplib.SMTP(smtp_server, 25)
            server.set_debuglevel(1)
            server.login(from_addr, password)
            server.sendmail(from_addr, [to_addr], msg.as_string())
            server.quit()


    #print type(result.loc[:len(result),['code','changepercent']])





remind()