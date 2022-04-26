import socket
import sys

import chatbuild

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5555
ERROR = "ERROR"
OK = "OK"
MAX_MSG_LENGTH = 1024
USERNAME = ""
client_socket = None


# HELPER SOCKET METHODS


def connect():
	"""
	Establishes a connection with the server and returns a socket ready for communication
	Paramaters: Nothing
	Returns: Nothing
	"""
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
	client_socket.connect((SERVER_IP, SERVER_PORT))  # connect to server
	return client_socket


def login():
	username = input("enter username: ")
	password = input("enter password: ")
	global client_socket
	msg=chatbuild.build_msg(chatbuild.CLIENT_COMMENDS [ "login" ] [ "cmd" ],
	                    chatbuild.CLIENT_COMMENDS [ "login" ] [ "code" ],
	                    [ username, password ])
	client_socket.send(msg.encode())


def main():
	global client_socket
	try:
		client_socket = connect()
		full_msg = "naor"
		login()
		while True:
			full_msg = input("enter: message: ")
			if full_msg == "exit":
				break
			if len(full_msg) < MAX_MSG_LENGTH:
				client_socket.send(full_msg.encode())
			else:
				print("ERROR: MAX_MSG_LENGTH")
		client_socket.close()
	except:
		client_socket.close()
		e = sys.exc_info()
		print(e)


if __name__ == "__main__":
	main()
