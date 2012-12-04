// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#ifndef D_Head_H
#define D_Head_H

#include "Arduino.h"

class Head
{
  private:
    int vinitpos;
    int hinitpos;
    int headstep;
    int srv1, srv2;

  public:

    Head(int srv, int srv2);
    boolean hup();
    void hdown(int);
    void hleft(int);
    void hright(int);
};

#endif
