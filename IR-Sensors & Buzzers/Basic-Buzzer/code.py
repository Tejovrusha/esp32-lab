from machine import Pin
import time

buzzer = Pin(23, Pin.OUT)

while True:
    buzzer.value(0)
    time.sleep(0.1)  
    buzzer.value(1)
    time.sleep(0.9)
