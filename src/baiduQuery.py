# # coding=utf-8
#
# import random
# import urllib2
# import datetime
# from BeautifulSoup import BeautifulSoup
#
# from pymongo import MongoClient
#
# client = MongoClient('mongodb://127.0.0.1:27017/')
# db = client.test
#
#
#
#
# def getHtml(keyword,rn="20"):
#     print keyword
#     url = 'http://www.baidu.com/ns?ct=1&rn='+rn+'&ie=utf-8&bs='+keyword.replace(" ","%20")+'&rsv_bp=1&sr=0&cl=2&f=8&prevct=no&tn=news&word='+keyword.replace(" ","%20")+'&ct=0&clk=sortbytime'
#     print url
#     user_agents = [
#         'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#         'Opera/9.25 (Windows NT 5.1; U; en)',
#         'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#         'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#         'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#         'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#         "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#         "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
#     ]
#     agent = random.choice(user_agents)
#     request = urllib2.Request(url)
#     request.add_header('User-Agent', agent)
#     request.add_header('Host', 'www.baidu.com')
#     request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
#     strs=""
#     try:
#         response = urllib2.urlopen(request, timeout=10)
#         strs = response.read().decode('utf-8')
#     except Exception, e:
#         print "重新连接"
#         getHtml(keyword)
#     return strs
#
# def dayStr_getTo():
#     date=datetime.datetime.now()
#     oneday = datetime.timedelta(days=1)
#     day = date - oneday
#     date_from = datetime.datetime(date.year, date.month, date.day,03,00)
#     return date_from.strftime("%Y年%m月%d日 %H:%M")
# def dayStr_getYesT():
#     date=datetime.datetime.now()
#     oneday = datetime.timedelta(days=1)
#     day = date - oneday
#     date_from = datetime.datetime(day.year, day.month, day.day,03,00)
#     return date_from.strftime("%Y年%m月%d日 %H:%M")
#
#
# def dayDate_getNow():
#     date=datetime.datetime.now()
#     date_from = datetime.datetime(date.year, date.month, date.day,date.hour,date.minute)
#     return date_from
#
# def dayDate_getTo():
#     date=datetime.datetime.now()
#     date_from = datetime.datetime(date.year, date.month, date.day,03,00)
#     return date_from
#
#
#
# def countNews(name,code,html):
#     nowTime = dayDate_getNow()
#     thTime = dayDate_getTo()
#     today = dayStr_getTo()
#     yestoday = dayStr_getYesT()
#     bs = BeautifulSoup(html)
#     result = bs.findAll('p', attrs={'class': 'c-author'});
#     count = 0
#     for i in result:
#         now = i.contents[0].encode("utf-8").split("&nbsp;&nbsp;")[1]
#         print now
#         if '前' in now:
#             hours = now.replace("小时前", "");
#             seconds = hours * 60 * 60
#             if seconds >= ((nowTime - thTime).total_seconds()):
#                 count += 1
#         else:
#             if (yestoday <= now <= today):
#                 count += 1
#
#     if count > 10:
#         newsCode = {
#             'NAME': name,
#             'CODE': code,
#             'COUNT': count
#         }
#         db.newsCode.insert(newsCode)
#         print newsCode
#
#
#
#
#
# def statisticalQuantity():
#     db.newsCode.drop()
#     for codes in db.stockCode.find():
#         name = codes.get('NAME').encode("utf-8")
#         code = codes.get('SYMBOL').encode("utf-8")
#         keywords = "\""+name.replace(" ", "") + ' ' + code+"\""
#         html = getHtml(keywords)
#         countNews(name,code,html)
#
#
#
#
#
#
# if __name__ == '__main__':
#     statisticalQuantity()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
