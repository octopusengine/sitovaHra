#!/usr/bin/python           # This is client.py file
import time, socket               # Import socket module
print("---client---")

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1212 #12345                # Reserve a port for your service.
print("host: "+host + " /"+str(port))

s.connect((host, port))

for x in range(1,10):
  msg=s.recv(1024)	
  print msg, str(len(msg)), "."+msg[:4]+"."
  if msg[:4]=="exit":
	  runData=False
	  print("konec")
	  s.close 
	  break
  time.sleep(5)

#s.close                     # Close the socket when done
print("conection - closed") 
