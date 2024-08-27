import requests

from gpiozero import LED, Button
from signal import pause
from time import sleep
URL = "https://maker.ifttt.com/trigger/With name/json/with/key/wXibIBusz16iQXQT8VBnq"
payload = dict(key1='value1', key2='value2')


button = Button(2)


def make_request():
    # r = requests.get(URL)
    r = requests.post(URL, data=payload)
    green = LED(17)
    blue= LED(27)
    green.on()
    sleep(5)
    green.off()
    blue.on()
    sleep(5)
    blue.off()
    print(r.status_code)

def light_shuffle():
    # r = requests.get(URL)
    r = requests.post(URL, data=payload)
    print(r.status_code)
    if (r.status_code == 200):
        green = LED(17)
        green.on()
        sleep(5)
        green.off()
    else:
        blue= LED(27)
        blue.on()
        sleep(5)
        blue.off()
    
button.when_pressed = light_shuffle



pause()
