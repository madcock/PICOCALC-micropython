import st7789
from machine import SoftI2C,Pin,UART,Timer,SPI
import time

tft=st7789.ST7789(
        SPI(2, baudrate=20000000, sck=Pin(39), mosi=Pin(36)),
        240,
        320,
        cs=Pin(37, Pin.OUT),
        dc=Pin(38, Pin.OUT),
        backlight=Pin(34, Pin.OUT),
        reset=Pin(40, Pin.OUT),
        rotation=3,
        color_order=st7789.RGB,
        inversion=False)

tft.init()      
tft.jpg('logo.jpg',0,0)