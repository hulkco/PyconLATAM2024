import time
from machine import Pin

# Configuring the LED Pin
led = Pin(6, Pin.OUT)
while (True):
    # Switch on the LED
    led.on()
    time.sleep_ms(500)
    # Switch off the LED
    led.off()
    time.sleep_ms(500)

