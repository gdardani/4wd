#!/usr/bin/python

from twisted.internet import protocol, reactor
from twisted.internet.serialport import SerialPort
from twisted.protocols import basic
import socket
import os
import time


class DeviceBluetooth(basic.Int16StringReceiver):

 def connectionMade(self):
  self.string = ""
  self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  self.socket.connect(('10.0.2.10',2003))
  
 def dataReceived(self, data):
  for x in data:
   x = x.rstrip(os.linesep)
   if x != '#':
    self.string+=x
   else:
    self.metricas = self.string.split(";")
    for met in self.metricas:
     s,value = met.split(":")
     message = s + " " + value + " " + str(int(round(float(time.time())))) + "\n"
     self.socket.send(message)
     message = ""
     self.string = ""

SerialPort(DeviceBluetooth(), '/dev/ttyACM1', reactor, baudrate=9600)
reactor.run()
