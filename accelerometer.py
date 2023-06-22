
import machine

xPin = 1 #A0
yPin = 2 #A1
zPin = 3 #A2

adcX = machine.ADC(machine.Pin(xPin))
adcY = machine.ADC(machine.Pin(yPin))
adcZ = machine.ADC(machine.Pin(zPin))

adcX.atten(machine.ADC.ATTN_11DB)
adcY.atten(machine.ADC.ATTN_11DB)
adcZ.atten(machine.ADC.ATTN_11DB)

while True:
    xValue = adcX.read()
    yValue = adcY.read()
    zValue = adcZ.read()
    
    print("X value: {:10}\tY value: {:10}\tZ value: {:5}".format(xValue, yValue, zValue))
