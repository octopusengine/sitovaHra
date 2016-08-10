#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
print("---server---")
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 1212 #12345                  # Reserve a port for your service.
print("host: "+host + " /"+str(port))

try:
  s.bind((host, port))        # Bind to the port
except:
  print("old conection - close:") 	
  s.close()	
  s.bind((host, port))

s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print 'Got connection from', addr
   c.send('Thank you for connecting. your server')
   for x in range(1,10):
	   
       msg=raw_input("?: ")
       c.send(msg+" >"+str(x))
   
   
   c.close()                # Close the connection
   
print("conection - closed")   
