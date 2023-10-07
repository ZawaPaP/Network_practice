import socket
import os


class Client:
    def __init__(self):
        self.server_ip = "127.0.0.1"
        self.server_port = 5008
        self.create_socket(self.server_ip, self.server_port)

    def create_socket(self, ip, port):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
        print("Connected to server at port {}".format(port))
        while True:
            message = self.input_message()
            client_socket.send(message.encode())
            if message == "quit":
                client_socket.close()
                break

    def input_message(self):
        message = input("Enter your message: ")
        return message


client = Client()
