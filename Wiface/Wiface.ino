/* Iface para comunicacao wifi com Arduino board
 gdardani - giovanidardani at gmail.com
 Python 2.7.3
 Version: 0.1 - 31/07/2012
*/

#include <WiServer.h>
 
#define WIRELESS_MODE_INFRA	1
#define WIRELESS_MODE_ADHOC	2
 
unsigned char local_ip[] = {10,0,0,50};	// IP address of WifiBee
unsigned char gateway_ip[] = {10,0,0,1};	// router or gateway IP address
unsigned char subnet_mask[] = {255,255,255,0};	// subnet mask for the local network
const prog_char ssid[] PROGMEM = {"Napalm"};	// max 32 bytes
 
unsigned char security_type = 3;	// 0 - open; 1 - WEP; 2 - WPA; 3 - WPA2
 
// WPA/WPA2 passphrase
const prog_char security_passphrase[] PROGMEM = {"NZ1oO7Vi"};	// max 64 characters
 
// WEP 128-bit keys
// sample HEX keys
prog_uchar wep_keys[] PROGMEM = { 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d,	// Key 0
				  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,	// Key 1
				  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,	// Key 2
				  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00	// Key 3
				};
 
// setup the wireless mode
// infrastructure - connect to AP
// adhoc - connect to another WiFi device
unsigned char wireless_mode = WIRELESS_MODE_INFRA;
unsigned char ssid_len;
unsigned char security_passphrase_len;

 
int counter;
// This is our page serving function that generates web pages
boolean sendMyPage(char* URL) {
 
    // Check if the requested URL matches "/"
    if (strcmp(URL, "/w") == 0) {
        WiServer.print(URL);
        Serial.println('119');
        //WiServer.print('0');
        return true;
    }
    if (strcmp(URL, "/s") == 0) {
        WiServer.print(URL);
        Serial.println('s');
        WiServer.print('0');
        return true;
    }
    if (strcmp(URL, "/a") == 0) {
        WiServer.print(URL);
        Serial.println('a');
        WiServer.print('0');
        return true;
    }
    if (strcmp(URL, "/d") == 0) {
        WiServer.print(URL);
        Serial.println('d');
        WiServer.print('0');
        return true;
    }
    if (strcmp(URL, "/q") == 0) {
        WiServer.print(URL);
        Serial.println('q');
        WiServer.print('0');
        return true;
    }
    if (strcmp(URL, "/e") == 0) {
        WiServer.print(URL);
        Serial.println('e');
        WiServer.print('0');
        return true;
    }
    // URL not found
    return false;
}
 
void setup() {
 
  // Initialize WiServer and have it use the sendMyPage function to serve pages
  WiServer.init(sendMyPage);
 
  // Enable Serial output and ask WiServer to generate log messages (optional)
  Serial.begin(9600);
  WiServer.enableVerboseMode(true);
}
 
void loop(){
  WiServer.server_task();
  delay(10);
}
