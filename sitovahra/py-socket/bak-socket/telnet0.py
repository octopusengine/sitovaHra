import sys
import telnetlib
HOST = "localhost"
user = "yenda"
password = "abc"

tn = telnetlib.Telnet(HOST, 8888, 5)
tn.write("login\r\n")
tn.write(user + "\r\n")
tn.write(password + "\r\n")
tn.write("rb 3\r\n") # this reboots plug 3
tn.write("rb 1\r\n") # this reboots plug 1
tn.write("logout\r\n")
tn.close

