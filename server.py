import socket
import queue
from threading import Thread

#si alguien se conecta debe ser guardado en clientes solamente si no esta en clientes
#para desconectarse debe mandar un codigo de desconxion
#para recivir mensajes el usuario (que anteriormente ya se habia conectado) se reconectara, el server esperara su mensaje 
#luego de eso lo debera reenviar globalmente el mensaje

class server():
    def __init__(self):
        self.s = socket.socket()
        self.host=socket.gethostname()
        self.port=7777

        self.addr=0
        self.c=0
        self.clients=[]
    
    def bind(self):
        self.s.bind((self.host, self.port))

    def wait_connection(self):
        self.s.listen(5)
        client=[]
        c, addr = self.s.accept()
        print("Got connection from", addr)
        return c
            
    def send_message(self, message, client):
        client.send(message.encode('utf-8'))

    def get_clients(self):
        return self.clients

    def send_global(self, message):
        for c in self.clients:
            print(c)
            c.send(message)
    
    def recv_message(self, client):
        message = client.recv(1024)
        return message
    
    def disconnect(self, client):
        client.close()
        self.clients.pop(self.clients.index(client))