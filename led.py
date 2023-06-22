
from machine import Pin
from time import sleep

led_pin = Pin(5, Pin.OUT)

while True:
    led_pin.on()
    print("HIGH")
    sleep(1)
    
    led_pin.off()
    print("LOW")
    sleep(1)
