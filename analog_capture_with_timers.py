
import machine
from machine import ADC, Timer
from time import sleep_ms
import sys

SENSOR_PIN = 1
MAX_READINGS = 10
readings = []
capture_timer = Timer(-1)
sensor_input = machine.ADC(machine.Pin(SENSOR_PIN))

def capture(_timer):
    print("capturing data")
    add_value()
    
def add_value():
    global readings
    if(len(readings) >= MAX_READINGS):
        readings.pop(0)
    readings.append(sensor_input.read_u16())
    print(readings)

capture_timer.init(mode = Timer.PERIODIC, period = 2000, callback = capture)

while (True):
    try:
        print("doing something...")
        if(len(readings) > 0 ):
            print(f"average value: {(sum(readings) / len(readings))}")
            pass
        sleep_ms(1000)
    except KeyboardInterrupt:
        print('program stopped')
        capture_timer.deinit()
        sys.exit(0)
