// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#include "hbridge.h"

Hbridge::Hbridge(
  int _en1,
  int _en2,
  int _en3,
  int _en4,
  int _ena,
  int _enb)
{
  last_dir = 0;
  en1 = _en1;
  en2 = _en2;
  en3 = _en3;
  en4 = _en4;
  ena = _ena;
  enb = _enb;

  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);
  pinMode(en3, OUTPUT);
  pinMode(en4, OUTPUT);
  pinMode(ena, OUTPUT);
  pinMode(enb, OUTPUT);
}

// move forward
void Hbridge::forward(int a, int b)
{
  if(last_dir == DFORWARD)
    return;

  digitalWrite(en1, LOW);
  digitalWrite(en2, HIGH);

  digitalWrite(en3, HIGH);
  digitalWrite(en4, LOW);

  speed(a, b);
  last_dir = DFORWARD;
}

// move backward
void Hbridge::backward(int a, int b)
{
  if(last_dir == DBACKWARD)
    return;
    
  digitalWrite(en1, HIGH);
  digitalWrite(en2, LOW);

  digitalWrite(en3, LOW);
  digitalWrite(en4, HIGH);

  speed(a, b);
  last_dir = DBACKWARD;
}

// turn left
void Hbridge::left(int a, int b)
{
  if(last_dir == DLEFT)
    return;
    
  digitalWrite(en1, HIGH);
  digitalWrite(en2, LOW);
  
  digitalWrite(en3, HIGH);
  digitalWrite(en4, LOW);
  
  speed(a, b); 
  last_dir = DLEFT;
}

// turn right
void Hbridge::right(int a, int b)
{

    if(last_dir == DRIGHT)
     return;

    digitalWrite(en1, LOW);
    digitalWrite(en2, HIGH);

    digitalWrite(en3, LOW);
    digitalWrite(en4, HIGH);
    
    speed(a, b);
    last_dir = DRIGHT;
}

// stop motors
void Hbridge::stop()
{

  if(last_dir == DSTOP)
     return

  digitalWrite(en1, LOW);
  digitalWrite(en2, LOW);

  digitalWrite(en3, LOW);
  digitalWrite(en4, LOW);

  speed(0,0);
  last_dir = DSTOP;
}

// speed direction of motors
boolean Hbridge::speed(int a, int b) {

  analogWrite(ena, a);
  analogWrite(enb, b);

  return true;
}

void Hbridge::setspeed(int newspeed) {

  stop();
  analogWrite(ena, newspeed);
  analogWrite(enb, newspeed);
}
 
