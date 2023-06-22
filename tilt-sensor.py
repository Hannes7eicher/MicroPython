
from machine import Pin
import utime

p2 = Pin(5, Pin.IN, Pin.PULL_DOWN)

while True:
    print(p2.value())
    utime.sleep(1)
