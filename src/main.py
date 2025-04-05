from machine import SoftI2C,Pin,UART,Timer,SPI
import time
from utils.drivers import KEYBOARD
from utils.drivers import SCREEN
from utils.fbconsole import FBConsole
import utils.settings as setting
import utils.color as color
import os
import st7789

set_dic=setting.load_setting()
NAME=set_dic['OWNER']

screen=SCREEN(320,320)
kb=KEYBOARD()
screen.tft.jpg('logo.jpg',0,40)
time.sleep(1)

import machine, sdcard, os
from machine import SPI,Pin
spitf=SPI(baudrate=2000000, sck=Pin(1), mosi=Pin(2),miso=Pin(42))

theme=color.COLOR_CANDY
scr = FBConsole(screen,bg_color=theme['bg'],fg_color=theme['font'])
os.dupterm(scr)

print('MPY CONSOLE ON PICOCALC by jd3096')
print('V1.02')
print('WELCOME! '+NAME)
try:
    tf = sdcard.SDCard(spitf,Pin(41))
    os.mount(tf, '/sd')
    os.listdir('/')
    print("LOAD SDCARD as '/sd'")
except:
    print('NO SDARD')
time.sleep(0.5)

def check_key(t):
    re=kb.check_key()
    if re!=None:
        if re[0]==3:
            if re[1]==10:
                ip=b'\r\n'
            else:
                ip=re[1].to_bytes(1,'big')
            scr._c=ip
            scr._press()

    
tim=Timer(-1)
tim.init(mode=Timer.PERIODIC, period=10, callback=check_key)





