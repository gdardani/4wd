#!/usr/bin/python

## Iface para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.4 - 10/07/2012

import serial
import time
import sys
import re

## Serial port
serPort = '/dev/ttyACM0'
rateLimit = '9600'
timeOut = 3

########################################################
## Abre con serial
########################################################

def openSerialConn (serPort, rateLimit, timeOut):

 try:
  bot0 = serial.Serial(serPort, rateLimit, timeout=timeOut)
  time.sleep(2)
  msg = bot0.readline()
  if (msg):
   print "Device says: {0}".format(msg)
   return bot0
 
 except Exception as err:
  print "Falha conn porta serial: {0}".format(err)
  exit (1)

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

