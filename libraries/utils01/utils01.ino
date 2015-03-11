// Author: Giovani <giovanidardani at gmail.com>
// Date: 14/07/2012

#include "utils.h"

// read serial data
int serial_read(void)
{
  int key;

  if (Serial.available() > 0) {
    key = Serial.read();

    return key;
  }

  return 0;
}

