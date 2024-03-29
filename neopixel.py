
from machine import Pin
from time import sleep
import neopixel

PIXEL_NUMBER = 10
np = neopixel.NeoPixel(Pin(5), PIXEL_NUMBER)

purple = (200, 0, 200)
black = (0, 0, 0)

np.fill(black)
np.write()

def ringUp():
    for i in range(0, PIXEL_NUMBER):
        np[i] = purple
        np.write()
        sleep(0.1)
        
def ringDown():
    for i in range(0, PIXEL_NUMBER):
        np[i] = black
        np.write()
        sleep(0.1)
        
def ringOff():
    for i in range(0, PIXEL_NUMBER):
        np[i] = black
    np.write()
    
def runPixelRun():
    while(1):
        ringUp()
        ringDown()
    
runPixelRun()
