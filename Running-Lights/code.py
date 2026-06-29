from machine import Pin
import time

led1=Pin(18, Pin.OUT)
led2=Pin(19, Pin.OUT)
led3=Pin(21, Pin.OUT)
led4=Pin(5, Pin.OUT)

leds=[led1, led2, led3, led4]

while True:
    for i in range(4):
        leds[i].on()
        time.sleep_ms(100)
    for i in range(4):
        leds[i].off()
        time.sleep_ms(100)
