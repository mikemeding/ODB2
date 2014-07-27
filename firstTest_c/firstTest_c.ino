// OBD
#include <Arduino.h>
#include <Wire.h>
#include <OBD.h>

// LCD
#include <LiquidCrystal.h>
#include <SPI.h>

COBD obd; // ODB variable
int rpm;

// initialize the library with the number of the sspin 
//(or the latch pin of the 74HC595)
LiquidCrystal lcd(10);

void setup() {
  // setup LCD
  lcd.begin(16, 2);
  lcd.print("initalizing...");
  
  // setup ODB
  obd.begin();
  while(!obd.init()); // loop until success
  lcd.clear();
  lcd.setCursor(0,0);
}

void loop() {
  if(obd.read(PID_RPM, rpm)) {
    lcd.print("RPM ");
    lcd.print(rpm);
    delay(10); // delay 10ms
    lcd.clear();  
  }
}
