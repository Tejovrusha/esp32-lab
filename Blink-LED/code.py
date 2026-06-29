from machine import Pin
import time

led=Pin(2, Pin.OUT)

while True:
    led.on()
    print("LED is ON")
    time.sleep(1)
    led.off()
    print("LED is OFF")
    time.sleep(1)
