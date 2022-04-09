##############################################################################
# server.py
##############################################################################

import socket
import select
import random

# GLOBALS
messages_to_send = []
users = {}
questions = {}
logged_users = {}  # a dictionary of client hostnames to usernames - will be used later

ERROR_MSG = "Error! "
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"
MAX_MSG_LENGTH = 1024


# HELPER SOCKET METHODS


def setup_socket():
    """
    Creates new listening socket and returns it
    Recieves: -
    Returns: the socket object
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
    server_socket.bind((SERVER_IP, SERVER_PORT))  # link ip and port
    server_socket.listen()
    print("Listening for client......")
    return server_socket


def main():

    print("Setting up server.....")
    server_socket = setup_socket()
    client_sockets = []
    while True:
        ready_to_read, ready_to_write, in_error = select.select(
            [server_socket] + client_sockets, [], []
        )
        for current_socket in ready_to_read:
            if current_socket is server_socket:
                (client_socket, client_address) = current_socket.accept()
                print("New client joined", client_address)
                client_sockets.append(client_socket)
            else:
                full_msg = current_socket.recv(MAX_MSG_LENGTH).decode()
                if full_msg != "":
                    print(full_msg)
                else:
                    break


# Implement code ...


if __name__ == "__main__":
    main()
