
from machine import Pin
import utime

p2 = Pin(5, Pin.IN)

while True:
    print(p2.value())
    utime.sleep(1)
