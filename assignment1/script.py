import paho.mqtt.client as mqtt  # Importing paho-mqtt library
import time  
import random
import math                                             

 
# Defining and generating the values
def payload():
    payload = "{"
    payload += "\"Humidity\":" + str(round(random.uniform(0, 100), 2)) + ","
    payload += "\"Temperature\":" + str(round(random.uniform(-50, 50), 1)) + ","
    payload += "\"Wind Direction\":" + str(round(random.uniform(0, 360), 1)) + ","
    payload += "\"Wind Intensity\":" + str(round(random.uniform(0, 100), 2)) + ","
    payload += "\"Rain Height\":" + str(round(random.uniform(0, 50), 2))
    payload += "}"
    return payload


# Access token are fundamental, in order to connect to our weather stations
ACCESS_TOKEN1 = 'NceJCtES1sm2vxzdfuFE'  
ACCESS_TOKEN2 = 'UEpGS0b1U8pyOxvXnRhA'  
    
# The IP and the port provided by Thingsboard in order to connect to their system 
IP = '127.0.0.1'
PORT = 1883  


# The on_connect function that allows the client to reach the broker...
def on_connect(client, userdata, rc, *extra_params):
   print('Connected with result code ' + str(rc))

   
# ...and the on_message to send the desired message (weather information)
def on_message(client, userdata, msg):
  print('Topic: ' + msg.topic + '\nMessage: ' + str(msg.payload))


# Clients setup
client1 = mqtt.Client()
client1.on_connect = on_connect  
client1.on_message = on_message  
client1.username_pw_set(ACCESS_TOKEN1)
client1.connect(IP, PORT, 1)
client1.loop_start()  

client2 = mqtt.Client()
client2.on_connect = on_connect  
client2.on_message = on_message  
client2.username_pw_set(ACCESS_TOKEN2)
client2.connect(IP, PORT, 1)
client2.loop_start()   

# Sending data
while True:
    # Defining 2 payloads for the 2 stations
    payload1 = payload()  
    payload2 = payload()  
    ret = client1.publish("v1/devices/me/telemetry", payload1)  
    ret = client2.publish("v1/devices/me/telemetry", payload2)  
    print("Please check LATEST TELEMETRY field of your devices")         
    print(payload1);
    print(payload2);
    time.sleep(10)  # Wait 10 seconds to let you appreciate the random generation
