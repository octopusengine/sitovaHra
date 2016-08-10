# -*- coding: utf-8 -*-
from socket import gethostname, gethostbyname #getIp
import subprocess

def getIp():
   try:
    arg='ip route list'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1]
   except:
     ipaddr ="ip.Err"
   #print "ip: " ip
   return ipaddr
   
import urllib2
import json  

def getBTC():
    bcfile = urllib2.urlopen("https://www.bitstamp.net/api/ticker/").read()
    jObj = json.loads(bcfile)
    #print str(jObj["timestamp"])
    #print str(jObj["last"])
    lastNum =int(float(jObj["last"]))
    return  lastNum
