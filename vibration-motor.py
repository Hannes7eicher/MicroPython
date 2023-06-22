
from machine import Pin, PWM
import time

# Pin connected to the Grove Vibration Motor
VIBRATION_PIN = 5

# Create a controllable Pin for the vibration motor
vibration_motor = PWM(Pin(VIBRATION_PIN))

# Function to control the vibration motor
def control_vibration_motor(duty_cycle, duration):
    vibration_motor.duty(duty_cycle)
    time.sleep(duration)
    vibration_motor.duty(0)

# Control the vibration motor
control_vibration_motor(512, 1)  # Run at half speed for 1 second
