#!/usr/bin/python
# coding=utf-8
import datetime
def getweek():
    i = datetime.datetime.now()
    # print ('今天是这周的第%s天 ' % i.strftime('%w'))
    return (i.strftime('%w'))

whattime =getweek()
print whattime


def dayStr_getTo():
    date=datetime.datetime.now()
    oneday = datetime.timedelta(days=1)
    day = date - oneday
    date_from = datetime.datetime(date.year, date.month, date.day,03,00)
    return date_from.strftime("%Y年%m月%d日 %H:%M")
def dayStr_getYesT():
    date=datetime.datetime.now()
    oneday = datetime.timedelta(days=1)
    day = date - oneday
    date_from = datetime.datetime(day.year, day.month, day.day,03,00)
    return date_from.strftime("%Y年%m月%d日 %H:%M")


def dayDate_getNow():
    date=datetime.datetime.now()
    date_from = datetime.datetime(date.year, date.month, date.day,date.hour,date.minute)
    return date_from

def dayDate_getTo():
    date=datetime.datetime.now()
    date_from = datetime.datetime(date.year, date.month, date.day,03,00)
    return date_from

def getWeek():
    date = datetime.datetime.now()
    # print ('今天是这周的第%s天 ' % date.strftime('%w'))
    return date.strftime('%w')


nowTime = dayDate_getNow()
thTime=dayDate_getTo()
today=dayStr_getTo()
yestoday=dayStr_getYesT()
date=datetime.datetime.now()