from machine import Pin, PWM
import time

led=PWM(Pin(2), 5000)

while True:
    for i in range(0, 1024):
        led.duty(i)
        time.sleep_ms(5)
