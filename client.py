import socket
'''import asyncio
import os, sys

s = socket.socket()
host = socket.gethostname()
port = 7777

while True:
    try:
        s.connect((host, port))
        print("connection established")
        break
    except:
        exit()

async def msg_recv():
    while True:
        try:
            message = s.recv(1024)
            print(message)
        except:
            asyncio.sleep(5)


while True:
    print("Elija opcion\n1) Send\n2) Recieve")
    asyncio.run(msg_recv())
    
    entry = input()
    
    if entry == '1':
        message = input()
        s.send(message.encode('utf-8'))
    else:
        print("opcion no aceptada")
s.close()'''

class client():
    def __init__(self):
        s = socket.socket()
        host = socket.gethostname()
        port = 7777

        self.s=s
        self.host=host
        self.port=port
    
    def connect(self):
        conexion = self.s.connect((self.host, self.port))
        return conexion

    def recv_message(self):
        message = self.s.recv(1024)
        return message

    def send_message(self, message):
        self.s.send(message.encode('utf-8'))

    def disconnect(self):
        self.s.close()