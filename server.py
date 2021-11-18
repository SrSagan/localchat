import socket
import queue
from threading import Thread


class server():
    def __init__(self):
        self.s = socket.socket()
        self.host=socket.gethostname()
        self.port=7777

        self.addr=0
        self.c=0
    
    def bind(self):
        self.s.bind((self.host, self.port))

    def wait_connection(self):
        self.s.listen(5)
        c, addr = self.s.accept()
        print("Got connection from", addr)
        self.addr=addr
        self.c=c
        
    
    def send_message(self, message):
        self.c.send(message.encode('utf-8'))
    
    def recv_message(self):
        message =self.c.recv(1024)
        return message
    
    def disconnect(self):
        self.c.close()