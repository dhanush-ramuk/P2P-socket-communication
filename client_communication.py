
from threading import Thread
import sys


class Client_Communication:

	def __init__(self):
		self.client_message = None
		
	
	def start_client_communication(self, client_socket):
		self.client_socket = client_socket
		self.send_client_thread = Thread(target=self.send_module_client, daemon=True)
		self.send_client_thread.start()
		self.receive_module_client()
		self.client_socket.close()
		sys.exit()
	
	
	def send_module_client(self):
		while True:
			self.client_message = input("")
			self.client_socket.send(self.client_message.encode())

			
	def receive_module_client(self):
		data = self.client_socket.recv(1024)
		while data.decode():
			if data.decode() == "exit()":
				break
			print("\033[01m\033[92m{}\033[0m".format(data.decode()))
			data = self.client_socket.recv(1024)
		return
