#!/usr/bin/python

## Iface para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.5 - 19/10/2012

import serial
import time
import sys
import re
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
timeOut = 3

########################################################
## Abre con serial
########################################################

def openSerialConn (serPort, rateLimit, timeOut):

 try:
  bot0 = serial.Serial(serPort, rateLimit, timeout=timeOut)
  time.sleep(3);

 except Exception as err:
  print "Falha conn porta serial: {0}".format(err)
  exit (1)

 msg = bot0.readline()

 if (msg):
  print "Device says: {0}".format(msg)

 return bot0
 
########################################################
## Le comando da porta serial, valida e envia cmd
########################################################

## Comandos conhecidos
command = {
 'q': 'stop',
 'w': 'forwd',
 's': 'backwd',
 'a': 'left',
 'd': 'right',
 'e': 'exit',
 'h': 'help',
 'c': 'set speed',
}

def RunCmd(sconn):

 ## Le input do teclado
 cmd = raw_input('cmd# ')

 ## valida comando
 if (cmd not in command):
  print "Comando '{0}' nao encontrado".format(cmd)
  sconn.write('q')

 ## Exit
 if (cmd == 'e'):
  try:
   sconn.write('q')
   print "Bye"
   exit (1)

  except Exception as err:
   print "Falha ao enviar comando STOP, conexao encerrada".format(err)
   exit (1)

 ## Help
 if (cmd == 'h'):
  for key in command:
   print "{0} -- {1}".format(key,command[key])

 ## Envia comando
 try:
  sconn.write(cmd)

 except Exception as err:
  print "Falha ao enviar comando: {0} -- {1}".format(command[cmd],err)



########################################################
## Main
########################################################

if __name__ == "__main__":

 sConn = openSerialConn(serPort, rateLimit, timeOut)
 if (sConn):
  while 1:
   RunCmd(sConn)

