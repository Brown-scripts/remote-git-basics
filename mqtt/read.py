import paho.mqtt.client as mqtt
from gpiozero import LED
from time import sleep


led=LED(17)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # personal topic on local env(127.0.0.1)
    # client.subscribe("lightSwitch")

    # subscribed to a general topic
    client.subscribe("glblcd/lightbulb")

    # created a topic on a general plat
    client.subscribe("glblcd/brown")


def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")
    if msg.payload.decode("utf-8")== 'on':
        led.on()
       
    elif msg.payload.decode("utf-8")== 'off':
        led.off()

    else:
        print('\nInvalid Input')

     
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message    

client.connect("mqtt.eclipseprojects.io", 1883, 60)

# connected to the local environment
# client.connect("127.0.0.1", 1883, 60)

client.loop_forever()



