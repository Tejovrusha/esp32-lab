from machine import Pin
import time

sensor=Pin(15, Pin.IN)
buzzer=Pin(23, Pin.OUT)
buzzer.value(1)

while True:
    if sensor.value()==0:
        buzzer.value(0)
        time.sleep(0.02)
        buzzer.value(1)
    time.sleep(0.5)
