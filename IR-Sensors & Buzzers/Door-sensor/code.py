from machine import Pin
import time

sensor=Pin(15, Pin.IN)
buzzer=Pin(23, Pin.OUT)
buzzer.value(1)
previous=current=1

while True:
    current=sensor.value()
    if current!=previous:
        buzzer.value(0)
        time.sleep(0.02)
        buzzer.value(1)
        previous=current
    time.sleep(0.5)
