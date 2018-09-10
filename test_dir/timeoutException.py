import urllib2
# http://classweb.loxa.com.tw/dino123/air/P1000772.jpg
r = urllib2.Request("http://classweb.loxa.com.tw/dino123/air/P1000775.jpg")
try:
        print 111111111111111111
        f = urllib2.urlopen(r, data=None, timeout=3)
        print 2222222222222222
        result =  f.read()
        print 333333333333333333
except Exception,e:
        print "444444444444444444---------" + str(e)

print "55555555555555"