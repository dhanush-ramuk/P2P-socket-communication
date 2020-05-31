#!bin/python3

import socket
import sys
import signal
import time
from communication_connection import Communication_Connection
from client_communication import Client_Communication
from server_communication import Server_Communication
from tcp_hole_punching_communication_connection import Tcp_Hole_Punch
from threading import Thread


class P2PChat:

	def __init__(self, port_number, receiver_ip):
		self.port_number = port_number
		self.receiver_ip = receiver_ip
		self.communication_connection_object = Communication_Connection(self.port_number)
		self.client_communication_object = Client_Communication()
		self.server_communication_object = Server_Communication()
		
	
	def create_socket(self):
		return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		
	def start_server(self):
		with self.create_socket() as sok:
			(self.server_socket, client_address) = self.communication_connection_object.connect_to_client(sok)
			print("Type \"exit()\" to close connection\nStart Chatting!\n")
			self.server_communication_object.start_server_communication(self.server_socket)
	
		
	def start_client(self):
		with self.create_socket() as sok:
			self.client_socket = self.communication_connection_object.connect_to_server(self.receiver_ip, sok)
			print("Type \"exit()\" to close connection\nStart Chatting!\n")
			self.client_communication_object.start_client_communication(self.client_socket)
			
	

		

if __name__ == "__main__":
	port_number = 2239
	if len(sys.argv) >= 2:
		if sys.argv[1] == "connect":
			p2pchat_object = P2PChat(port_number, sys.argv[2])
			p2pchat_object.start_client()
	
	else:
		p2pchat_object = P2PChat(port_number, None)
		p2pchat_object.start_server()
