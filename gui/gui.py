#!/usr/bin/python

## Iface para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.1

from Tkinter import *
import serial

## Serial port
serPort = '/dev/null'
#serPort = '/dev/ttyUSB0'
rateLimit = '9600'
timeOut = 3

########################################################
## Serial Conn
########################################################

class SerialConn():
 def __init__(self):
 #def __init__(self,serPort, rateLimit, timeOut):
  self.serPort=serPort
  self.rateLimit=rateLimit
  self.timeOut=timeOut
  try:
   self.bot0 = serial.Serial(self.serPort, self.rateLimit, self.timeOut)
   time.sleep(3);
  except Exception as err:
   print "Falha conn porta serial: {0}".format(err)
   exit (1)

class Application(Frame):
 def sendCommando(self):
  print "hi there, everyone!"

 def createWidgets(self):
  self.conn = SerialConn()
  self.left = Button(self)
  self.left["text"] = '<--'
  self.left["fg"]   = "blue"
  self.left["command"] =  self.quit
  self.left.pack({"side": "left"})

  #self.hi_there = Button(self)
  #self.hi_there["text"] = "Hello",
  #self.hi_there["command"] = self.say_hi
  #self.hi_there.pack({"side": "left"})

 def __init__(self, master=None):
  Frame.__init__(self, master)
  self.pack()
  self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
