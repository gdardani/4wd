// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#include "p4wd.h"
#include "utils.h"
#include "hbridge.h"

#define EN1 8
#define EN2 9
#define EN3 12
#define EN4 13
#define ENA 10
#define ENB 11

#define SPEED 200

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
  };
};
  
  
void setup()
{
  Serial.begin(9600);
  Serial.println("ON --> Running ...");
  hbridge.stop();
}

void loop()
{ 
  int cmd = serial_read();
  Run_Cmd(cmd);
  delay(300);
}

