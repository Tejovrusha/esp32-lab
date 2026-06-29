from machine import Pin
import time

sensor=Pin(15, Pin.IN)
led=Pin(2, Pin.OUT)

while True:
    if sensor.value()==0:
        led.value(not led.value())
    time.sleep_ms(75)
