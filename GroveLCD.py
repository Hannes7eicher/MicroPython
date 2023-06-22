
import machine
from time import sleep
from machine import I2C, Pin
from i2c_lcd import Display


i2c = machine.I2C(sda=machine.Pin(12), scl=machine.Pin(11))
display = Display(i2c, lcd_addr = 0x3e)

display.clear()
display.write('Hello,')
sleep(0.5)
display.move(0, 1)
sleep(0.5)
display.write('World!')
