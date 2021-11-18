import socket
import queue
from threading import Thread


class client():
    def __init__(self):
        s = socket.socket()
        self.s=s
        self.host=socket.gethostname()
        self.port=7777
    
    def connect(self):
        self.s.connect((self.host, self.port))

    def recv_message(self):
        message =self.c.recv(1024)
        return message

    def send_message(self, message):
        self.s.send(message.encode('utf-8'))

    def disconnect(self):
        self.s.close()