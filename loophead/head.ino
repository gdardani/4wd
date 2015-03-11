// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#include "head.h"

Head::Head()
{
//  int vinitpos = 90;
//  int hinitpos = 90;
//  int headstep = 2;
}

// move forward
void Head::hup()
{
  vinitpos = vinitpos + headstep;
  if ( vinitpos >= 180){
   vinitpos = 180;
   srv1.write(vinitpos);
  }
  Serial.print("UP");
  Serial.println(vinitpos);
}

// move backward
void Head::hdown()
{
  vinitpos = vinitpos - headstep;
  srv1.write(vinitpos);
  Serial.print("DOWN");
  Serial.println(vinitpos);
}

// turn left
void Head::hleft()
{
  hinitpos = hinitpos - headstep;
  srv2.write(hinitpos);
  Serial.print("LEFT");
  Serial.println(hinitpos);
}

// turn right
void Head::hright()
{
  hinitpos = hinitpos + headstep;
  srv2.write(hinitpos);
  Serial.print("RIGHT");
  Serial.println(hinitpos);
}

// stop motors
void Head::hreset()
{
  srv1.write(89);
  srv2.write(89);
}


