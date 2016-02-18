#!/usr/bin/python
# by yang.l
import sys
import time
if len(sys.argv)==2:
        a1=(sys.argv[1])
        if(len(a1)==8):
                result1=int(time.mktime(time.strptime(a1, '%Y%m%d'))*1000)
        else:
                result1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(a1)/1000))
        print result1
elif len(sys.argv)==3:
        a1=(sys.argv[1])
        a2=(sys.argv[2])
        result1=int(time.mktime(time.strptime(a1, '%Y%m%d')))
        result2=(int(time.mktime(time.strptime(a2, '%Y%m%d')))+86400-1)
        print "[%d000 to %d999]" %(result1,result2)
else:
        print 'error.'
        sys.exit()
