import socket
import sys

SERVER_IP = "127.0.0.1"  # Our server will run on same computer as client
SERVER_PORT = 5555
ERROR = "ERROR"
OK = "OK"
MAX_MSG_LENGTH = 1024
USERNAME = ""

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



def main():
    client_socket=0
    try:
        client_socket = connect()
        full_msg="naor"
        if len(full_msg) < MAX_MSG_LENGTH:
            client_socket.send(full_msg.encode())
            print("send")
        else:
           print("MAX_MSG_LENGTH")
        client_socket.close()
    except:
        client_socket.close()
        e = sys.exc_info()
        print(e)


if __name__ == "__main__":
    main()
