from time import localtime, sleep, time
import paho.mqtt.client as mqtt
from blinkt import set_pixel, show, clear


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("DSM/timer/test")
    
def on_message(client, userdata, msg):
    global t, status
    allowed_status = ["active","abort"]

    message=msg.payload.decode('UTF-8')

    split_message=message.split()

    error=True
    
    if len(split_message)==2:
        if split_message[0].isdigit():
            split_message[0]=int(split_message[0])
            if split_message[1] in allowed_status:
                error=False

    if error==True:
        print("SOMETHING FUCKED UP")
        return

    t=split_message[0]
    status=split_message[1]

    

#**** GLOBAL VARIABLES ****

t=0
status="stop"
previous_status="stop"

#**** MQTT Setup ****

client = mqtt.Client(protocol='MQTTv311')
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.5", 1883, 60)

client.loop_start()

#count=int(input("Enter the seconds: "))
#timer(count)

#**** Main loop ****

print(time())
print(time()+10)

sleep(10)


print(time())

while True:
    if t>0:
        time_remaining=t-time()
        print(time_remaining)
        if time_remaining>=0:
            print(time_remaining)
            print(t)
            if status=="active":
                print("Countdown",time_remaining)
                mins,secs = divmod(time_remaining,60)
                print("t =",time_remaining)
                print(mins,secs)
                lights=[]
                if time_remaining>=60:
                    if mins>=128:
                        lights.append("green")
                        mins=mins-128
                    else:
                        lights.append(0)
                    if mins>=64:
                        lights.append("green")
                        mins=mins-64
                    else:
                        lights.append(0)
                    if mins>=32:
                        lights.append("green")
                        mins=mins-32
                    else:
                        lights.append(0)
                    if mins>=16:
                        lights.append("green")
                        mins=mins-16
                    else:
                        lights.append(0)
                    if mins>=8:
                        lights.append("green")
                        mins=mins-8
                    else:
                        lights.append(0)
                    if mins>=4:
                        lights.append("green")
                        mins=mins-4
                    else:
                        lights.append(0)
                    if mins>=2:
                        lights.append("green")
                        mins=mins-2
                    else:
                        lights.append(0)
                    if mins>=1:
                        lights.append("green")
                        mins=mins-1
                    else:
                        lights.append(0)
                    print(lights)
                elif time_remaining>8:
                    if secs>=128:
                        lights.append("amber")
                        secs=secs-128
                    else:
                        lights.append(0)
                    if secs>=64:
                        lights.append("amber")
                        secs=secs-64
                    else:
                        lights.append(0)
                    if secs>=32:
                        lights.append("amber")
                        secs=secs-32
                    else:
                        lights.append(0)
                    if secs>=16:
                        lights.append("amber")
                        secs=secs-16
                    else:
                        lights.append(0)
                    if secs>=8:
                        lights.append("amber")
                        secs=secs-8
                    else:
                        lights.append(0)
                    if secs>=4:
                        lights.append("amber")
                        secs=secs-4
                    else:
                        lights.append(0)
                    if secs>=2:
                        lights.append("amber")
                        secs=secs-2
                    else:
                        lights.append(0)
                    if secs>=1:
                        lights.append("amber")
                        secs=secs-1
                    else:
                        lights.append(0)
                    print(lights)
                elif time_remaining>=1:
                    for i in range(8,0,-1):
                        if i>t:
                            lights.append(0)
                        else:
                            lights.append("red")
                    print(lights)
                #t-=1
                sleep(1)
            elif status=="abort":
                print("Stopping...")
                clear()
                show()
                t=0
                time_remaining=0
        else:
            t=0
            time_remaining=0
    
