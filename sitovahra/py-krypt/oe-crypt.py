# -*- coding: utf-8 -*-
#http://tkinter.programujte.com/

import time
import subprocess
from threading import Thread 
from Tkinter import *

import md5
#pip install pycrypto 
from Crypto import Random
from Crypto.Cipher import AES
import base64
BLOCK_SIZE=32

from oeLib import *
main = Tk()

w = Canvas(main, width=505, height=280)
w.pack()

mainF="Verdana"
mainFsize=" 10 "
mainFont=mainF+mainFsize
mainFontb=mainF+mainFsize+"bold"
mainFonti=mainF+mainFsize+"italic"
mainFontbi=mainF+mainFsize+"bold italic"

tb=Text(font=mainFont) #text block
tb.tag_config("blu",  foreground="blue", underline=0)
tb.tag_config("sil",  foreground="maroon", underline=0)
tb.tag_config("help", background="silver", foreground="maroon", font="verdana 10")
tb.tag_config("n1",   background="yellow", foreground="blue", font="verdana 10 bold")

nexThread = True #running


#("Times", 10, "bold")
#("Helvetica", 10, "bold italic")
#("Symbol", 8)
# fixedis 
i00=0.1
nas=250

def hello():
    print "Ahoj!"

def cmHelp():
    tb.delete(1.0, END)
    tb.insert(END, "Help\n", "n1")
    
    f = open('help.txt', 'r')
    helpText=f.read()
    tb.insert(END, helpText, "help")
    tb.insert(END, "\n", "help")
    tb.insert(END, "continue\n", "n1")

def cmAbout():
    tb.delete(1.0, END)
    tb.insert(END, "About\n", "n1")
    
    f = open('about.txt', 'r')
    abText=f.read()
    tb.insert(END, abText, "help")
    tb.insert(END, "\n", "help")
    tb.insert(END, "continue\n", "n1")



def callback1():
    print "Kliknul jsi 1"

def callback2():
    #print "Kliknul jsi 2"
    tb.insert(END, "click \n")
    #tb.pack()

def readTxt():
    print vstup.get()
    tb.insert(END, vstup.get())
    tb.insert(END, " \n")
    c1=md5.new(vstup.get()).digest()
    c2=md5.new(vstup.get()).hexdigest()
    print c2
    tb.insert(END, c1+" \n")
    tb.insert(END, c2+" \n")
    hex_abc="900150983cd24fb0d6963f7d28e17f72"
    hex_123="202cb962ac59075b964b07152d234b70"
    if (c2==hex_abc):
        tb.insert(END, "OK)abc \n") 
    if (c2==hex_123):
        tb.insert(END, "OK)123 \n")  
   
   
def ipBTC():
   #for i in range(10):
   #  tb.insert(END,"\n")
   #  tb.insert(END,str(i))
   #   w.create_line(0, 0, 100+i*nas, 100-i*nas)
   tb.delete(1.0, END)  
   tb.insert(END, getIp())
   tb.insert(END, getBTC())
  

def f1():
   #for i in range(10):
   #  tb.insert(END,"\n")
   #  tb.insert(END,str(i))
   #   w.create_line(0, 0, 100+i*nas, 100-i*nas)
   tb.delete(1.0, END)  
   # tb.insert(END, getIp())
   # tb.insert(END, getBTC())
   tb.insert(END, "AES test \n") 
   
   print("AES test")
   obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
   message = "The answer is no"
   ciphertext = obj.encrypt(message)
   print ciphertext
   tb.insert(END,ciphertext)
   obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
   tb.insert(END,obj2.decrypt(ciphertext))
  
   
def f2(): 
    #arg='ip route list'
    arg='ls -lha'
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    #tsplit_data = data[0].split()
    #tipaddr = split_data[split_data.index('src')+1]
    tb.insert(END, data, "help")   
    
     
def f3(): #realna parabola
 global i00 	
 i0=i00
 for ii in range(100):
   #print ii
   i1=4*i0*(1-i0)
   #print ii, i1
   tb.insert(END, str(ii)+"..."+str(i1)+"\n")
   w.create_rectangle(ii*5, i1*nas,ii*5+5, i1*nas+5,fill="red")
   i0=i1
 i00=i0


def f5(): #realna parabola
 global i00 	
 i0=i00
 for num in range(100):
  for ii in range(100):
   #print ii
   i1=4*i0*(1-i0)
   #print ii, i1
   tb.insert(END, str(ii)+"..."+str(i1)+"\n")
   w.create_rectangle(ii*5, i1*nas,ii*5+5, i1*nas+5,fill="orange")
   i0=i1
  i00=i0
  
  
def nexth(): ##thread
 global nxRead, nexThread 
 cntx=0 
 while nexThread:

   
   time.sleep(5)
   cntx=cntx+1 
   print cntx 
  
def canvasCls():
	nic=True 

#---thread start
thrnx = Thread(target=nexth)
thrnx.start()




hlavniMenu = Menu(main)
menuSoubor = Menu(hlavniMenu, tearoff=0)
hlavniMenu.add_cascade(label="File", menu=menuSoubor)

menuUpravy = Menu(hlavniMenu, tearoff=0)
hlavniMenu.add_cascade(label="Edit", menu=menuUpravy)

menuText = Menu(hlavniMenu, tearoff=0)
hlavniMenu.add_cascade(label="Text block", menu=menuText)
menuText.add_command(label="IP / BTC", command=ipBTC)
menuText.add_command(label="F1 - AES", command=f1)
menuText.add_command(label="F2", command=f2)

menuCanvas = Menu(hlavniMenu, tearoff=0)
hlavniMenu.add_cascade(label="Canvas", menu=menuCanvas)
menuCanvas.add_command(label="F3 - stocha", command=f3)
menuCanvas.add_command(label="F5 - 30stocha", command=f5)
menuCanvas.add_separator()
menuCanvas.add_command(label="clear", command=canvasCls)


menuNapoveda = Menu(hlavniMenu, tearoff=0)
hlavniMenu.add_cascade(label="Help", menu=menuNapoveda)

# vytvořit rozbalovací menu a přidat ho k hlavnímu menu

menuSoubor.add_command(label="Open", command=hello)
menuSoubor.add_command(label="Save", command=hello)
menuSoubor.add_separator()
menuSoubor.add_command(label="Quit", command=main.quit)



# další rozbalovací menu

menuUpravy.add_command(label="Cut", command=hello)
menuUpravy.add_command(label="Copy", command=hello)
menuUpravy.add_command(label="Paste", command=hello)
menuUpravy.add_separator()
menuUpravy.add_command(label="F3 - stocha", command=f3)
menuUpravy.add_command(label="F5 - 30stocha", command=f5)


menuNapoveda.add_command(label="About", command=cmAbout)
menuNapoveda.add_command(label="Help", command=cmHelp)


# zobrazení menu
main.config(menu=hlavniMenu)


tb.insert(END, "text... ")
tb.insert(END, "block")

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(5, 5))
w.create_rectangle(10, 10, 15, 15, fill="silver")

i0=0.2
for ii in range(50):
   i1=4*i0*(1-i0)
   w.create_rectangle(ii*5, i1*100,ii*5+5, i1*100+5,fill="silver")
   i0=i1





tb.pack()
   

b1 = Button(main, text="First command - terminal", command=callback1, font=mainFonti)
b2 = Button(main, text="Second command - text block", command=callback2, font=mainFont)

vstup = Entry(main)
vstup.pack()
vstup.focus_set()

b3 = Button(main, text="Read", width=10, command=readTxt, font=mainFontb)

b1.pack()
b2.pack()
b3.pack()
#b1.grid(row=2, column=1)
#b2.grid(row=2, column=2)
#b3.grid(row=2, column=3)


for i in range(10):
     tb.insert(END,"\n","sil")
     tb.insert(END,str(i))
     w.create_line(0, 0, 200+i*2, 100-i*2)
     
tb.insert(END, "\n IP: "+getIp())
tb.insert(END, "\n BTC: "+str(getBTC()))     
tb.insert(END, "\n"
)       
     


mainloop()









