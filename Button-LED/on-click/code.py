from machine import Pin
import time

button=Pin(0, Pin.IN, Pin.PULL_UP)
led=Pin(2, Pin.OUT)

while True:
    if(button.value()==0):
        led.on()
        print("Button is pressed")
        time.sleep(0.25)
    else:
        led.off()
