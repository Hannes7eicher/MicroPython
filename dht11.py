
import dht
from machine import Pin
from time import sleep_ms

SENSOR_PIN = 5

TEMP_SENSOR = dht.DHT11(Pin(SENSOR_PIN))
sleep_ms(500)

while(1):
    TEMP_SENSOR.measure()
    print(TEMP_SENSOR.temperature())
    print(TEMP_SENSOR.humidity())
    sleep_ms(1000)
