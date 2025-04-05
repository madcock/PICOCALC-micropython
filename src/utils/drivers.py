#ST7789
from machine import Pin, SPI, freq
import st7789

class SCREEN():
    def __init__(self, width, height):
        custom_init = [
        (b'\x01', 100),                  # soft reset
        (b'\xCF\x00\xC1\x30',),
        (b'\xED\x64\x03\x12\x81',),      # power on sequence control
        (b'\xE8\x85\x00\x78',),     # driver timing control A
        (b'\xCB\x39\x2C\x00\x34\x02',),  # power control A
        (b'\xF7\x20',),            # pump ratio control
        (b'\xEA\x00\x00',),     # driver timing control B
        (b'\xC0\x23',),            # power control,VRH[5:0]
        (b'\xC1\x10',),            # Power control,SAP[2:0];BT[3:0]
        (b'\xC5\x3E\x28',),        # vcm control
        (b'\xC7\x86',),            # vcm control 2
        (b'\x37\x00',),            # madctl
        (b'\x3A\x55',),            # pixel format
        (b'\xB1\x00\x18',),        # frameration control,normal mode full colours
        (b'\xB6\x02\x02',),       # display function control
        (b'\xF2\x00',),            # 3gamma function disable
        (b'\x26\x01',),            # gamma curve selected
        # set positive gamma correction
        (b'\xE0\x0F\x31\x2B\x0C\x0E\x08\x4E\xF1\x37\x07\x10\x03\x0E\x09\x00',),
        # set negative gamma correction
        (b'\xE1\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F',),
        (b'\x21', 50),    
        (b'\x11', 100),                  # display on
        (b'\x29', 100),                  # display on
        ]
    
        custom_rotations = [
            (0x88, 320, 320, 0, 0),
            (0xE8, 320, 320, 0, 0),
            (0x48, 320, 320, 0, 0),
            (0x28, 320, 320, 0, 0),
        ]

        self.tft=st7789.ST7789(
        SPI(1, baudrate=40000000, sck=Pin(35), mosi=Pin(36)),
        320,
        320,
        cs=Pin(38, Pin.OUT),
        dc=Pin(39, Pin.OUT),
        reset=Pin(40,Pin.OUT),
        custom_init=custom_init,
        rotation=2,
        color_order=st7789.RGB,
        inversion=False,
        options=0,
        rotations=custom_rotations,
        buffer_size=0)
        self.tft.init()
        self.tft.fill(0)

#BC6561 KEYBOARD
from machine import I2C,Pin
import time

class KEYBOARD():
    def __init__(self):
        scp=Pin(18,Pin.IN,Pin.PULL_UP)
        sdp=Pin(17,Pin.IN,Pin.PULL_UP)
        self.i2c = I2C(1, scl=scp, sda=sdp, freq=10000)

    def check_key(self):
        data = self.i2c.readfrom_mem(31, 0x09,2)
        return data
    

            

            
    



