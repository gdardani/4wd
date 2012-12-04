// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#include "head.h"
#include <Servo.h>

Head::Head(
  int _srv1,
  int _srv2)
{
  pinMode(srv1, OUTPUT);
  pinMode(srv2, OUTPUT);
  
  Servo srv1;
  Servo srv2;
  srv1.attach(_srv1);
  srv2.attach(_srv2);
}

// move forward
boolean Head::hup()
{
  vinitpos = vinitpos + headstep;
  srv1.write(vinitpos);
}

// move backward
void Head::down(int a)
{
  vinitpos = vinitpos - headstep;
  svr1.write(vinitpos);
}

// turn left
void Head::hleft(int a, int b)
{
  hinitpos = hinitpos - headstep;
  svr2.write(hinitpos);
}

// turn right
void Head::hright(int a)
{
  hinitpos = hinitpos - headstep;
  svr2.write(hinitpos);
}

// stop motors
boolean Hbridge::hreset()
{
   svr1.write(89);
   svr2.write(89);
   return true
}
)

