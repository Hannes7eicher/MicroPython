
from machine import Pin, ADC
import time

pin_adc = ADC(Pin(5))
pin_adc.atten(ADC.ATTN_11DB)

while True:
    sum_value = 0
    for i in range(32):
        sum_value += pin_adc.read()

    sum_value >>= 5

    print(sum_value)
    time.sleep_ms(10)
