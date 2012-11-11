#!/usr/bin/python

## Iface para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.1

import pygtk
pygtk.require('2.0')
import gtk
import serial
import time
from optparse import OptionParser

########################################################
## cli parser
########################################################

usage = (
        "Usage: %prog --d <device> -s <speed>"
)

cparser = OptionParser(usage=usage, version="%prog 0.5")
cparser.add_option("--d", "--device", action="store", type="str", dest="device", help="Serial device - ex: /dev/ttyUSB0", default='/dev/ttyUSB0')
cparser.add_option("--s", "--speed", action="store", type="str", dest="speed", help="Serial Speed ex: 9600", default='9600')
opts, args = cparser.parse_args()

## Serial port
serPort = opts.device
rateLimit = opts.speed
timeOut = '3'

########################################################
## Serial Conn
########################################################

class sendCmd:

 def __init__(self):
  try:
   self.bot = serial.Serial(serPort, rateLimit)
   #self.bot = serial.Serial(serPort, rateLimit, timeOut)
   time.sleep(3);
   
  except Exception as err:
   print "Falha conn porta serial: {0}".format(err)

 def fwd(self, bla, bla1):
  try:
   self.bot.write('w')
  except Exception as err:
   print "Falha enviar comando: {0}".format(err)

 def stop(self, bla, bla1):
  try:
   self.bot.write('q')
  except Exception as err:
   print "Falha enviar comando: {0}".format(err)

class Application:

 def frente(self, widget, data=None):
  self.button1.connect("clicked", self.conn.fwd, None)

 def tras(self, widget, data=None):
  self.button2.connect("clicked", self.conn.stop, None)

 def __init__(self):
  self.conn = sendCmd()
  self.window1 = gtk.Window(gtk.WINDOW_TOPLEVEL)
  self.window2 = gtk.Window(gtk.WINDOW_TOPLEVEL)
  self.button1 = gtk.Button(label="f")
  self.button2 = gtk.Button(label="s")
  self.button1.connect("clicked", self.frente, None)
  self.button2.connect("clicked", self.tras, None)
  self.window1.add(self.button1)
  self.window2.add(self.button2)
  
  self.button1.show()
  self.button2.show()
  self.window1.show()
  self.window2.show()


 def main(self):
  gtk.main()

if __name__ == "__main__":
 app = Application()
 app.main()
