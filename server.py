import socket

#si alguien se conecta debe ser guardado en clientes solamente si no esta en clientes
#para desconectarse debe mandar un codigo de desconxion
#para recivir mensajes el usuario (que anteriormente ya se habia conectado) se reconectara, el server esperara su mensaje 
#luego de eso lo debera reenviar globalmente el mensaje

class server():
    def __init__(self):
        self.s = socket.socket()
        self.host=socket.gethostname()
        self.port=7777

        self.names=[]
        self.clients=[]
        self.hosts=[]
    
    def bind(self):
        self.s.bind((self.host, self.port))

    def wait_connection(self):
        self.s.listen(5)
        c, addr = self.s.accept()
        if c not in self.clients:
            self.clients.append(c)
        print("Got connection from", addr)
        return c
        
    def send_message(self, message, client):
        client.send(message.encode('utf-8'))
    
    def add_name(self, name):
        self.names.append(name)
    
    def add_host(self, host):
        self.hosts.append(host)

    def get_clients(self):
        return self.clients

    def send_global(self, message, sender):
        for c in self.clients:
            try: 
                index = self.hosts.index(sender)
                endmessage = self.names[index]+": "+message
            except:
                endmessage = sender+": "+message
                
            c.send(endmessage.encode('utf-8'))
    
    def send_event(self, message):
        for c in self.clients:
            c.send(message.encode('utf-8'))
    
    def recv_message(self, client):
        message = client.recv(1024)
        return message
    
    def disconnect(self, client):
        client.close()
        self.clients.pop(self.clients.index(client))