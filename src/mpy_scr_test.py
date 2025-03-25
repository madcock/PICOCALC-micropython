"""ILI9488 demo (fonts)."""
from time import sleep
from ili9488 import Display, color565
from machine import Pin, SPI
import random

def test():
    """Test code."""
    # Baud rate of 60000000 seems about the max
    spi = SPI(1, baudrate=60000000, sck=Pin(10), mosi=Pin(11))
    display = Display(spi, dc=Pin(14), cs=Pin(13), rst=Pin(15))
    display.draw_circle(100, 100,20, color565(0, 255, 0))


test()
