
from threading import Thread
import sys

class Server_Communication:

	def __init__(self):
		self.server_message = None
		
	def start_server_communication(self, server_socket):
			self.server_socket = server_socket
			self.send_server_thread = Thread(target=self.send_module_server, daemon=True)
			self.send_server_thread.start()
			self.receive_module_server()
			self.server_socket.close()
			sys.exit()
	
	def send_module_server(self):
		while True:
			self.server_message = input("")
			self.server_socket.send(self.server_message.encode())

			
	def receive_module_server(self):
		data = self.server_socket.recv(1024)
		while data.decode():
			if data.decode() == "exit()":
				break
			print("\033[01m\033[92m{}\033[0m".format(data.decode()))	
			data = self.server_socket.recv(1024)			
		return
