#include <dht11.h>

dht11 DHT11;

#define DHT11PIN 2

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int chk = DHT11.read(DHT11PIN);
  if(chk == 0) {
   Serial.print("H:");
   Serial.print((float)DHT11.humidity, 2);
   Serial.print(";"); 
   Serial.print("T:");
   Serial.print((float)DHT11.temperature, 2);
   Serial.print("#");
   delay(2000);
  } 
}

