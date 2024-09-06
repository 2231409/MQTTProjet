import time

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, reason_code, properties):
    print("hello")
    client.subscribe("YounesCristelle/#")
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc =mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("10.4.1.144", 1883, 60)

while True:
    mqttc.loop()
    time.sleep(1)