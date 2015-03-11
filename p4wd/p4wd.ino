// Author: Giovani <giovanidardani at gmail.com>
// Date: 13/11/2012

#include "p4wd.h"
#include "utils.h"
#include "hbridge.h"
#include "head.h"
#include <Servo.h>

// Engines
#define EN1 8
#define EN2 9
#define EN3 12
#define EN4 13
#define ENA 10
#define ENB 11
#define SRV1 3
#define SRV2 5

//min and max engines speed
int HB_SPEED_MIN = 80;
int HB_SPEED_MAX = 220;
// default engines speed
int SPEED = 80;
// increase and deecrease speed
int SPEED_STEP = 20;
Servo srv1;
Servo srv2;
int vinitpos = 90;
int hinitpos = 90;
int headstep = 2;

Hbridge hbridge(EN1, EN2, EN3, EN4, ENA, ENB);
Head head;

void Run_Cmd(int cmd) {
  
  switch (cmd){

    //bfoward (w)
    case 119:
     hbridge.forward(SPEED,SPEED);
     break;
    
    //bbackward (s) 
    case 115:
     hbridge.backward(SPEED,SPEED);
     break;
     
    //bleft (a)
    case 97:
     hbridge.left(SPEED,SPEED);
     break;
    
    //bright (d) 
    case 100:
     hbridge.right(SPEED,SPEED);
     break;
     
    //bstop (q) 
    case 113:
     hbridge.stop();
     break;
     
   //bspeed up (z) 
    case 122:
     hbridge.setspeed(0);
     break;

    //bspeed down(x)     
    case 120:
     hbridge.setspeed(1);
     break;
    
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
  hbridge.stop();
}

void loop()
{ 
  int cmd = serial_read();
  //Serial.println(cmd);
  //delay(300);
  Run_Cmd(cmd);
}
