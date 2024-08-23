from gpiozero import LED,Button
from time import sleep

led_red= LED()
led_yellow=LED()
led_green=LED()
button=Button()

while button.when_pressed:
    led_red.on
    sleep(2)
    led_red.off
    led_yellow.on
    sleep(2)
    led_yellow.off
    led_green.on
    sleep(2)
    led_green.off


