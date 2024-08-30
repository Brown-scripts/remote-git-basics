import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:
        print("Connection failed")

Connected = False  # global variable for the state of the connection

client = mqtt.Client()
client.on_connect = on_connect
client.connect("mqtt.eclipseprojects.io", 1883, 60)
# client.connect("127.0.0.1", 1883, 60)
client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

try:
    while True:
        message = input('Your message: ')
        # publishing to only those subscibed to my personal topic using local env
        # client.publish("lightSwitch", message)

        # client.publish("glblcd/lightbulb", message)
        client.publish("glblcd/register", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()