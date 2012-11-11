#!/usr/bin/python

## Gui para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.2

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
   time.sleep(3);
   
  except Exception as err:
   print "Falha conn porta serial: {0}".format(err)
   exit (1)

 def set_mov(self, mov):
  try:
   self.bot.write(mov)
  except Exception as err:
   print "Falha enviar comando: {0}".format(err)
 
class Application:

 def setmov_callback(self, mov, foo):
  self.conn.set_mov(mov)

 def delete_event(self, widget, event, data=None):
  gtk.main_quit()
  return False

 def __init__(self):
  self.conn = sendCmd()
  self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  self.window.set_title("4WD - Gui ")
  self.window.connect("delete_event", self.delete_event)
  self.window.set_border_width(20)
 
  self.box = gtk.VBox(False, 0)
  self.window.add(self.box)

  self.button1 = gtk.Button("FORWARD")
  self.button2 = gtk.Button("BACKWARD")
  self.button3 = gtk.Button("LEFT")
  self.button4 = gtk.Button("RIGHT")

  self.button1.connect_object("button_press_event", self.setmov_callback, "w")
  self.button1.connect_object("button_release_event", self.setmov_callback, "q")

  self.button2.connect_object("button_press_event", self.setmov_callback, "s")
  self.button2.connect_object("button_release_event", self.setmov_callback, "q")

  self.button3.connect_object("button_press_event", self.setmov_callback, "a")
  self.button3.connect_object("button_release_event", self.setmov_callback, "q")

  self.button4.connect_object("button_press_event", self.setmov_callback, "d")
  self.button4.connect_object("button_release_event", self.setmov_callback, 'q')

  self.box.pack_start(self.button1, True, True, 0)
  self.box.pack_start(self.button2, True, True, 0)
  self.box.pack_start(self.button3, True, True, 0)
  self.box.pack_start(self.button4, True, True, 0)

  self.button1.show()
  self.button2.show()
  self.button3.show()
  self.button4.show()

  self.box.show()
  self.window.show()

 def main(self):
  gtk.main()

if __name__ == "__main__":
 app = Application()
 app.main()
