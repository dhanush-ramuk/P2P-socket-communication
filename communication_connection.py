import socket
import time
import sys

class Communication_Connection:

	def __init__(self, port_number):
		self.waitTime = 0
		self.connection_tries = 10
		self.port_number = port_number	
		
	def connect_to_client(self, sok):
		flag = 0
		sok.bind(('', self.port_number))
		print("waiting for client connection...")
		while True:
			try:
				sok.listen()
				sok.settimeout(5)
				(client_connection_object, client_address) = sok.accept()
				print("{} connected".format(client_address[0]))
				break
			except socket.timeout:
				if flag == 0:
					print("\nCannot establish connection. Client is not online or probably not running this application. Make the client run this script with your IP address to connect to to you. \n\nExample on their side \"python3 communication.py SEND <your_ip_address>\"")
					time.sleep(3)
					flag = 1
				self.repeat_connection_tries()
		return (client_connection_object, client_address)
				
	def connect_to_server(self, receiver_ip, sok):
		flag = 0
		while True:
			try:
				sok.connect((receiver_ip, self.port_number))
				print("Connection established to {}".format(receiver_ip))
				break
			except ConnectionRefusedError:
				if flag == 0:
					print("\nConnection cannot be established to {}. They are not online or probably not running this application. Make them run this script. \n\nExample on their side \"python3 communication.py\"".format(receiver_ip))
					flag = 1
				self.repeat_connection_tries()
		return sok
				
	
	def repeat_connection_tries(self):
		print("\nTrying to establish connection again in 3 seconds. {} tries remaining".format(self.connection_tries))
		time.sleep(3)
		self.connection_tries = self.connection_tries - 1
		self.waitTime = self.waitTime + 5
		if(self.waitTime == 50):
			print("\nSorry! Connection cannot be established. Exiting...")
			sys.exit() 
