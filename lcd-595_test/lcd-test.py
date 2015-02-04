#!/bin/python
### ------Shift Register 74HC595 PinOut------
### [SR Pin 14 (DS) Pin6, of LCD shield] to RasPi GPIO - [datapin]
### [SR Pin 12 (ST_CP), Pin4 of LCD shield] to RasPi GPIO - [latchpin]
### [SR Pin 11 (SH_CP)], Pin3 of LCD shield to Raspi GPIO - [clockpin]
### Black wire to Ground, Pin1 of LCD Shield
### Red wire to +5v, Pin2 of LCD Shield
### Pin4 of LCD Shield, DNC 
###
### ------Shift Reg to LCD-----
### SR physical Pin: --- LCD Pin:
### SR Pin 15 --- ENABLE 10000000
### SR Pin 1 --- D7             00000010
### SR Pin 2 --- D6            00000100
### SR Pin 3 --- D5 00001000
### SR Pin 4 --- D4 00010000
### SR Pin 5 --- not connected 00100000
### SR Pin 6 --- backlight control 01000000
### SR Pin 7 --- RS 00000001
### lcdHome (const int fd) ;
### lcdClear (const int fd) ;
### lcdDisplay (const int fd, int state) ;
### lcdCursor (const int fd, int state) ;
### lcdCursorBlink (const int fd, int state) ;
### lcdSendCommand (const int fd, unsigned char command) ;
### lcdPosition (const int fd, int x, int y) ;
### lcdCharDef (const int fd, int index, unsigned char data [8]) ;
### lcdPutchar (const int fd, unsigned char data) ;
### lcdPuts (const int fd, const char *string) ;
### lcdPrintf (const int fd, const char *message, ...) ;
### lcdInit (const int rows, const int cols, const int bits,
from wiringpi2 import *
import time
wiringPiSetupGpio() # use RasPi GPIO pin scheme
# Set data, latch and clock pin
dataPin = 17
latchPin = 27
clockPin = 22
# Set pins to Output Mode - 5 Volts should never be used for Input!
pinMode(dataPin, 1)
pinMode(latchPin, 1)
pinMode(clockPin, 1)
# Assign values to 595's output pins (0 - 7)
pinBase = 100
#LED = pinBase + 6
RS = pinBase + 7
E = pinBase + 0
DB4 = pinBase + 4
DB5 = pinBase + 3
DB6 = pinBase + 2
DB7 = pinBase + 1
# pinBase, num pins used, SER, SRCLK, RCLK
sr595Setup(pinBase, 8, dataPin, clockPin, latchPin)
# Init HD44780 LCD's pins
# RS, E, DB4, DB5, DB6 and DB7's signals are coming out of the 595
#lcd = lcdInit(2, 16, 4, RS, E, 0, 0, 0, 0, DB4, DB5, DB6, DB7)
lcd = lcdInit(2, 16, 4, RS, E, DB4, DB5, DB6, DB7, 0, 0, 0, 0)
#def BKL(ENABLE):
# digitalWrite(LED, ENABLE)
def INIT():
 lcdHome(lcd)
 lcdClear(lcd)
 #lcdPuts(lcd, time.strftime("%d-%m-%y - %H:%M"))
def PRINT(text, col, row):
 lcdPosition(lcd, col, row)
 lcdPrintf(lcd, text)
