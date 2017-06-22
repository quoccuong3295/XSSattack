import requests
import httplib
from bs4 import BeautifulSoup
import socket
import re
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

print (" 1. footprinting and reconnaissance ")
print (" 2. xss vulnerability scanner ")
choice = raw_input(' Enter your choice [1-2] : ')

if('1' in choice):
    print "usage: mydtu.duytan.edu.vn"
    remoteServer = raw_input("Please enter the website: ")
    remoteServerIP = socket.gethostbyname(remoteServer) #get name address divices
    temp = remoteServer.split('://')[-1]
    print temp
    print "-" * 60
    print "Please wait...i'm scanning remote host", remoteServerIP
    print "-" * 60

    # Check what time the scan started
    t1 = datetime.now()

    try:
        for port in(21,22,25,80,81,443):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port)) #connect to port
            if(result == 0):
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


    url="https://dig.whois.com.au/ip/"+remoteServer
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
    
if('2' in choice):
    sql = ['<script>alert(XSS)</script>','<script>prompt(XSS)</script>'
       '<script>alert(String.fromCharCode(120, 115, 115))</script>',
       '%3Cscript%3Ealert%28XSS%29%3C%2fscript%3E',
       '<ScRipT>AlERt(XsS)</ScRipT>',
       '"><script>alert(XSS)</script>',
       '<scri%00pt>alert(1);</scri%00pt>']
    
    print"Please select the sql query as your expected number..."

    try:
        #site = sys.argv[1]
        site = raw_input("Enter the target: ")
        #Get the root of site: Ex. Input "www.hinshawmusic.com/search_results.php?keyword=greer" then the root_url will be "www.hinshawmusic.com"
        root_url = site.split('/')[0]
        print "root_url: %s" %root_url
            
        #Get the extension of site: Ex. Input "www.hinshawmusic.com/search_results.php?keyword=greer" then the extension will be "/search_results.php?keyword=greer"
        extension_url = site.split('/')[-1]
        print "extension_url: %s" %extension_url
        print "web site for scan: http://%s" % root_url
        conn1 = httplib.HTTPConnection(root_url)
        conn1.connect()
        print "Connect to webserver on port 80"

        print "Start scanning site"
        print "--------- List SQL injection ---------"
        count = 1

        for xss in sql:
            print "SQL %s: "%count
            print "%s"%xss
            count=count+1 #tang len moi lan ket thuc vong lap

        select = 1
        while select!=0:
                select = int(raw_input("Please select SQL/Select 0 to exit: "))
                xss = sql[select]

                if select!=0:
                        print "Check For Find XSS Of Is Site %s :" % root_url
                        conn2 = httplib.HTTPConnection(root_url)
                        print "Connect To Page : %s" % root_url
                        conn2.request("GET","/%s" %extension_url)
                                    
                        response = conn2.getresponse()
                            
                        print "responese.status = %s" %response.status
                        print "XSS: %s" %xss
                                
                        if response.status == 404:
                            print "\033[91mNot Found (404) URL For XSS On Site:  \033[0m"
                            print "Display JavaScript On site:      %s     " % xss
                            print "****************************************"
                                    
                        elif response.status == 200:
                            print "\033[91mFound XSS On Site:  \033[0m" 
                            print " "
                            print "Display JavaScript On site:      %s     " % xss
                            print "*********************************************************"
             
                        elif response.status == 305:
                            print "\033[91mUse Proxy (since HTTP/1.1)\033[0m"
                            print "Display JavaScript On site:      %s     " % xss
                            print "*********************************************************"
                        elif response.status == 400:
                            print "\033[91mBad Request\033[0m"
                            print "Display JavaScript On site:      %s     " % xss
                            print "*********************************************************"
                       
                       
                        elif response.status == 500:
                            print "\033[91m500 Internal Server Error\033[0m"
                            print "Display JavaScript On site:      %s     " % xss
                        elif response.status == 505:
                            print "\033[91mHTTP Version Not Supported\033[0m"
                            print "Display JavaScript On site:      %s     " % xss
                            print "*********************************************************"
                        elif response.status == 521:
                            print "\033[91mWeb server is down\033[0m"
                            print "Display JavaScript On site:      %s     " % xss
                      


                        else:
                            print "Exit Program"
                            print "Count Site Scan : %s " %count
                else:
                        print "System exit"
                        sys.exit()

            
    except KeyboardInterrupt:
        print "Press + C"
        sys.exit()

    







    
