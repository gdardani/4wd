#!/usr/bin/python

## Iface para comunicacao serial com Arduino board
## gdardani - giovanidardani at gmail.com
## Python 2.7.3
## Version: 0.2 - 10/07/2012

import serial
import time
import sys

## Serial port
serPort = '/dev/ttyACM0'
rateLimit = '9600'
timeOut = 3

## Comandos conhecidos
command = {
 'q': 'stop',
 'w': 'forwd',
 's': 'backwd',
 'a': 'left',
 'd': 'right',
 'e': 'exit',
 'h': 'help'
}

try:
 # abre conn serial e espera ate estar estabelecida (~ 2s)
 bot0 = serial.Serial(serPort, rateLimit, timeout=timeOut)
 time.sleep(2)
 msg = bot0.readline()
 if (msg):
  print "Device says: {0}".format(msg)
 
except Exception as err:
 print "Falha conn porta serial: {0}".format(err)
 exit (1)

while 1:
 cmd = raw_input('cmd# ')

 if (cmd not in command):
  print "Comando '{0}' nao encontrado".format(cmd)
  continue

 if (cmd == 'e'):
  try:
   bot0.write('q')
   print "Bye"
   break

  except Exception as err:
   print "Falha ao enviar comando STOP, conexao encerrada".format(err)
   exit (1)


 if (cmd == 'h'):
  for key in command:
   print "{0} -- {1}".format(key,command[key])

 try:
  bot0.write(cmd)

 except Exception as err:
  print "Falha ao enviar comando: {0} -- {1}".format(command[cmd],err)
