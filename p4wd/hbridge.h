// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#ifndef D_HBRIDGE_H
#define D_HBRIDGE_H

#include "Arduino.h"

enum {
  DSTOP=1, DFORWARD, DBACKWARD, DLEFT, DRIGHT};

class Hbridge
{
  private:
    int last_dir;
    int en1, en2, en3, en4, ena, enb;

  public:

    Hbridge(int en1, int en2, int en3, int en4, int ena, int enb);
    void forward(int, int);
    void backward(int, int);
    void left(int, int);
    void right(int, int);
    boolean setspeed(int);
    void stop(void);
    boolean speed(int, int);
    //min and max engines speed
    #define HB_SPEED_MIN 60
    #define HB_SPEED_MAX 220
    // default engines speed
    #define SPEED 120
};

#endif
