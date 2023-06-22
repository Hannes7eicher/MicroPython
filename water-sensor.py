
from machine import Pin
import time

signal_pin = Pin(5, Pin.IN)
prev_sensor_value = None

while True:
    signal_value = signal_pin.value()
    
    if signal_value != prev_sensor_value:
        if signal_value == 0:
            print("Vibration")
        else:
            print("No Vibration")
