#!/usr/bin/python

## Gui(no buttons) para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.2.1

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

cparser = OptionParser(usage=usage, version="%prog 0.2.1")
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

  global bodyctl
  global speedctl
  global headctl
  global displaymov
  bodyctl = {'w': 'w', 's': 's', 'a':'a', 'd':'d','q': 'q'} 
  speedctl = {'Page_Down': 'x','Page_Up': 'z'}
  headctl = {'Up': 'h', 'Down': 'i', 'Left': 'l', 'Right': 'r'}
  displaymov = {'w': 'Forward', 's': 'Backward', 'a': 'Lefth', 'd': 'Right', 'q': 'Stop', 'Page_Down': 'Speed Down', 'Page_Up': 'Speed Up'}

  try:
   ##time out nao funciona
   self.bot = serial.Serial(serPort, rateLimit)
   time.sleep(3);
   
  except Exception as err:
   print "Falha conn porta serial: {0}".format(err)
   exit (1)

 def set_mov(self, mov):

  try:
   if mov in bodyctl:
    self.bot.write(bodyctl[mov])

   if mov in speedctl:
    self.bot.write(speedctl[mov])

   if mov in headctl:
    self.bot.write(headctl[mov])

  except Exception as err:
   print "Falha enviar comando: {0}".format(err)

  return False

class Application:

 def on_key_press_event(self, widget, event):
  self.cmd = gtk.gdk.keyval_name(event.keyval)
  if self.cmd in displaymov:
   self.label.set_markup(displaymov[self.cmd])
   self.label.set_label(displaymov[self.cmd])
  self.conn.set_mov(self.cmd)

 def on_key_release_event(self, widget, event):
  if gtk.gdk.keyval_name(event.keyval) not in speedctl and gtk.gdk.keyval_name(event.keyval) not in headctl:
   self.conn.set_mov('q')
  self.label.set_label('')

 def delete_event(self, widget, event, data=None):
  gtk.main_quit()
  return False

 def __init__(self):
  self.conn = sendCmd()
  self.cmd = 'q'

  self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
  self.window.set_position(gtk.WIN_POS_CENTER)
  self.window.set_default_size(200,50)
  self.window.set_title("4WD - Gui ")
  self.window.connect("delete_event", self.delete_event)
  self.window.set_border_width(10)
  self.box = gtk.HBox(True, 0)
  self.window.add(self.box)
  self.label = gtk.Label(str=None)
  self.box.pack_start(self.label, True, True, 0)

  self.window.connect_object("key_press_event", self.on_key_press_event, None)
  self.window.connect_object("key_release_event", self.on_key_release_event, None)
  self.window.show_all()

 def main(self):
  gtk.main()

if __name__ == "__main__":
 app = Application()
 app.main()
