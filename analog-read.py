
import machine

pot_pin = 2  # A0
adc = machine.ADC(machine.Pin(pot_pin))
adc.atten(machine.ADC.ATTN_11DB)  # Set attenuation level for the ADC

while True:
    pot_value = adc.read()
    print("Potentiometer value:", pot_value)
