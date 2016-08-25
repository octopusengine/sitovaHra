#!bin/usr/env python
"""Let's make some sockets!"""
import time, socket
from time import ctime
import threading

##Server Socket##

print("---server---")
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1212 #12345          # Reserve a port for your service.
print("host: "+host + " /"+str(port))

sADDR = (host, port)
buff = 1024
rMessage=""


try:
  servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servSock.bind(sADDR)
  
except:
  print("old conection - close:") 	
  servSock.close()
  time.sleep(1)	
  servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  servSock.bind(sADDR)
servSock.listen(5)


print "Waiting for a connection..."
cliSock, cADDR = servSock.accept()
print "...Connection made with {0}".format(cADDR)

def receive():
    global rMessage
    while True:
        rMessage = cliSock.recv(buff)
        if not rMessage:
            print "Ending connection"
            break
        print "[{0}]: {1}".format(ctime(), rMessage)

def send():
    while True:
        sMessage = raw_input(">>")
        if not sMessage:
            break
        cliSock.send(sMessage)


def sendAuto():
    global rMessage
    while True:
		if len(rMessage)>1:
			sMessage = " >> ok:"+str(int(rMessage)*2)
			cliSock.send(sMessage)
			rMessage=""

t1 = threading.Thread(target=sendAuto, name=3)
t2 = threading.Thread(target=receive, name=4)

t1.start()
t2.start()

