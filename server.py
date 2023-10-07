import socket
# https://docs.python.org/3/library/socket.html
# socket — Low-level networking interface
# This module provides access to the BSD socket interface.

BACKLOG = 5
BUFFER_SIZE = 1024


class Server:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 5008
        self.create_socket(self.ip, self.port)

    def create_socket(self, ip, port):
        # create an INET, STREAMing socket
        self.server_socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a public host, and a well-known port
        self.server_socket.bind((ip, port))
        # become a server socket
        self.server_socket.listen(BACKLOG)
        print("Server is listening on port {}".format(port))

    def accept_connections(self):
        while True:
            print("Waiting for connection...")
            # accept connections from outside
            (client_socket, address) = self.server_socket.accept()
            print("Connection from {}".format(address))

            while True:
                # receive message from client
                data = client_socket.recv(BUFFER_SIZE).decode()
                if data == "quit":
                    client_socket.close()
                    print("Connection closed")
                    break
                print("Received message: {}".format(data))
                client_socket.send(data.encode())


server = Server()
server.accept_connections()
