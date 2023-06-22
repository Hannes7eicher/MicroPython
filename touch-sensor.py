
from machine import Pin

touch_pin = Pin(5, Pin.IN)
prev_sensor_value = None

while True:
    sensor_value = touch_pin.value()

    if sensor_value != prev_sensor_value:
        if sensor_value == 1:
            print("Touch")
        else:
            print("No touch")
        
        prev_sensor_value = sensor_value
