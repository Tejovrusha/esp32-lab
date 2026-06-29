from machine import Pin
import time

red=Pin(18, Pin.OUT)
yellow=Pin(19, Pin.OUT)
green=Pin(21, Pin.OUT)

while True:
    red.value(1)
    time.sleep(3)
    red.value(0)
    yellow.value(1)
    time.sleep(1)
    yellow.value(0)
    green.value(1)
    time.sleep(3)
    green.value(0)
    time.sleep(1)
