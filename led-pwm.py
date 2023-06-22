
import machine
import time

led_pin = 5  # Pin connected to the LED

# Configure PWM on the LED pin
led_pwm = machine.PWM(machine.Pin(led_pin))
led_pwm.freq(1000)  # Set PWM frequency

# Fade the LED in and out
while True:
    for duty_cycle in range(1024):
        led_pwm.duty(duty_cycle)
        time.sleep(0.001)  # Adjust the delay to control the fading speed

    for duty_cycle in range(1023, -1, -1):
        led_pwm.duty(duty_cycle)
        time.sleep(0.001)  # Adjust the delay to control the fading speed
