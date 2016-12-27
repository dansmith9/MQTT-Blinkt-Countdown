from time import time
import paho.mqtt.publish as publish

duration=input("Enter the number of seconds: ")
duration=int(duration)+int(time())
print(duration)

message=str(duration)+" "+"active"

publish.single("DSM/timer/test", message, hostname="192.168.1.5", protocol="MQTTv311")

