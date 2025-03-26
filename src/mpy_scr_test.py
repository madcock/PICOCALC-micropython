from machine import SoftI2C,Pin,UART,Timer,SPI
import time
from utils.drivers import KEYBOARD
from utils.drivers import SCREEN
from utils.fbconsole import FBConsole
import utils.dos_font as font
import utils.settings as setting
import utils.color as color
import os
import st7789

set_dic=setting.load_setting()
NAME=set_dic['OWNER']

screen=SCREEN(320,320)
kb=KEYBOARD()
screen.tft.jpg('logo.jpg',0,40)
screen.tft.write(font,'screen test',0,0)