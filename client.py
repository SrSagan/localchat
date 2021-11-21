import socket

class client():
    def __init__(self):
        s = socket.socket()
        self.s=s
        self.host=socket.gethostname()
        self.port=7777
        self.connected=False
    
    def connect(self, host):
        self.s.connect((host, self.port))
        #return conexion

    def recv_message(self):
        message =self.s.recv(1024)
        return message

    def send_message(self, message):
        print(self.connected)
        message=message+"/-/"+self.host
        print(message)
        self.s.send(message.encode('utf-8'))

    def disconnect(self):
        self.s.close()

    def get_connected(self):
        return self.connected
    
    def set_connected(self, status):
        self.connected = status