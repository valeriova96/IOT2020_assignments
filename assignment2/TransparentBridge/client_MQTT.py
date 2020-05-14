import paho.mqtt.client as paho  		    									#Import paho-mqtt library	

#A gateway to send the received messages over MQTTSN to Thingsboard
class Gateway:
	def __init__(self,ACCESS_TOKEN1 = 'yc0CoSWmeQa9282OrDrz', ACCESS_TOKEN2 = 'jBbJuPNoYUUJmOtM4ec9',\
		 broker = 'demo.thingsboard.io',port = 1883):
		print("Connecting to MQTT Thingsboard Broker:")
		self.client1= paho.Client(client_id="client1")							
		self.client2= paho.Client(client_id="client2")							                   			
		self.client1.on_publish = self.on_publish 								
		self.client2.on_publish = self.on_publish 								
		self.client1.username_pw_set(ACCESS_TOKEN1)		
		self.client2.username_pw_set(ACCESS_TOKEN2) 	
		self.client1.connect(broker,port,keepalive=60)  			
		self.client2.connect(broker,port,keepalive=60) 				
		print('--------Connection with Thingsboard successful!--------')

	def on_publish(client,userdata,result):													
		print('Data have been published\n')
		pass
    	
	def publish1(self,payload): 															
		ret= self.client1.publish('virtualstation1/weather',payload) 
		print(payload)		
		print('--------Values successfully published!--------')
	
	def publish2(self,payload): 															
		ret= self.client2.publish('virtualstation2/weather',payload) 
		print(payload)		
		print('--------Values successfully published!--------')
		
   	def disconnect(self):																	
   		self.client.disconnect()
   		print('disconnected from MQTT broker')
