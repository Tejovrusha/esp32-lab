from machine import Pin, time_pulse_us
import time

led=Pin(2, Pin.OUT)
trigger=Pin(23, Pin.OUT)
echo=Pin(32, Pin.IN)

trigger.value(0)
time.sleep_us(5)

def get_distance():
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    duration=time_pulse_us(echo,1,50000)
    if duration<0:
        return -1
    return (duration*0.0343)/2

while True:
    distance = get_distance()
    if distance >= 0:
        print(f"Distance: {distance:.2f} cm")
        if distance <= 5:
            led.value(1)
        else:
            led.value(0)
    else:
        print("Sensor error or out of range")
    time.sleep(1)
