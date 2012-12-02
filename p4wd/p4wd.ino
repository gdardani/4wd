// Author: Giovani <giovanidardani at gmail.com>
// Date: 13/11/2012

#include "p4wd.h"
#include "utils.h"
#include "hbridge.h"

// Engines
#define EN1 8
#define EN2 9
#define EN3 12
#define EN4 13
#define ENA 10
#define ENB 11
//min and max engines speed
int HB_SPEED_MIN = 80;
int HB_SPEED_MAX = 220;
// default engines speed
int SPEED = 80;
// increase and deecrease speed
int SPEED_STEP = 20;


Hbridge hbridge(EN1, EN2, EN3, EN4, ENA, ENB);

void Run_Cmd(int cmd) {
  
  switch (cmd){

    //foward (w)
    case 119:
     hbridge.forward(SPEED,SPEED);
     break;
    
    //backward (s) 
    case 115:
     hbridge.backward(SPEED,SPEED);
     break;
     
    //left (a)
    case 97:
     hbridge.left(SPEED,SPEED);
     break;
    
    //right (d) 
    case 100:
     hbridge.right(SPEED,SPEED);
     break;
     
    //stop (q) 
    case 113:
     hbridge.stop();
     break;
     
   //seep up (z) 
    case 122:
     hbridge.setspeed(0);
     break;

    // seed down(x)     
    case 120:
     hbridge.setspeed(1);
     break;
  };
};
  
  
void setup()
{
  Serial.begin(SERIAL_SPEED);
  hbridge.stop();
}

void loop()
{ 
  int cmd = serial_read();
  Run_Cmd(cmd);
}
