import requests
from bs4 import BeautifulSoup
import socket
import subprocess
import sys
from datetime import datetime

import urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import urllib
from urllib import FancyURLopener
import cookielib
import time
import re
import sys
import httplib
import colorama
import ssl
from functools import partial
import custom
from colorama import Fore, Back, Style
from colorama import init


print "usage: http://www.santien.net"

remoteServer = raw_input("Please enter the website: ")

temp = remoteServer.split('://')[-1]
remoteServerIP = socket.gethostbyname(temp) #get name address divices


print "-" * 60
print "Please wait...Scanning remote host", remoteServerIP
print "-" * 60

# Check what time the scan started
t1 = datetime.now()

try:
    for port in(21,22,25,80,81,443):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        result = sock.connect_ex((remoteServerIP, port)) #connect to port

        if(result == 0) :
            print 'port {} is open'.format(port)
        sock.close()
except KeyboardInterrupt:
    print "You pressed Ctrl+C"
    sys.exit()

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    print "Couldn't connect to server"
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print 'Scanning Completed in: ', total

print "="*25,"$INFOMATION$", "="*25


url="https://dig.whois.com.au/ip/"+temp
r=requests.get(url)

soup=BeautifulSoup(r.content, "html.parser")

links=soup.find_all("pre")

for link in links:
   # print "<a href='%s'>%s</a>" %(link.get("href"), link.text)
   print link.text

#g_data=soup.find_all("div", {"class": "two-thirds column"})

#for item in g_data:
#   print item.contents[0].find_all("p", {"pre"})[0].text
    
                                          
print "=" * 28,"End", "="*28


colorama.init()

class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11'
       
myopener = MyOpener()
 
 
class fake_ssl:
    wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl.PROTOCOL_SSLv3)
 
httplib.ssl = fake_ssl
 
 
class JSHTTPCookieProcessor(urllib2.BaseHandler):
    handler_order = 400


#remoteServer = raw_input(" Enter A Vulnerable Link: ")
res = myopener.open(remoteServer)
res1= urllib.urlopen(remoteServer)
html = res.read()
links = re.findall('"((http|href)s?://.*?)"', html)


print res.info()
#myfile = res.read()





    
