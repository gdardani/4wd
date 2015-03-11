// Author: Giovani <giovanidardani at gmail.com>
// Date: 13/11/2012


#include "utils01.h"
#include "head.h"
#include "loophead.h"
#include <Servo.h>

// Engines
#define SRV1 9
#define SRV2 11

Servo srv1;
Servo srv2;
int vinitpos = 90;
int hinitpos = 90;
int headstep = 4;

Head head;

void Run_Cmd(int cmd) {
  
  switch (cmd){

    //hup (h)
    case 104:
     head.hup();
     break;
    
    //hdown (i)
    case 105:
     head.hdown();
     break;
    
    //hleft (l)
    case 114:
     head.hright();
     break;
    
    //hdown (r)
    case 108:
     head.hleft();
     break;

  };
};
  
  
void setup()
{
  Serial.begin(SERIAL_SPEED);
  pinMode(SRV1, OUTPUT);
  pinMode(SRV2, OUTPUT);
  srv1.attach(SRV1);
  srv2.attach(SRV2);
}

void loop()
{ 
  int cmd = serial_read();
  //Serial.println(cmd);
  delay(100);
  Run_Cmd(cmd);
}
