import server
import threading

server = server.server()

#TODO el server recivira y administrara el resto de clientes
#tiene que estar constantemente esperando conexiones y guardandolas (quiza en una array de clientes)
#si el cliente envia cierto codigo borrarlo de la lista de clientes activos

threads=[]
server.bind()
class recieve_messages(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        while True:
            message = server.recv_message(self.client)
            message = message.decode('utf-8')
            if(message == "/disconnect"):
                server.disconnect(self.client)
                break
            elif("/name" in message):
                x = message.find("/name")
                if(x == 0):
                    name = message[x+6:]
                    server.add_name(name)
            else:
                server.send_global(message, client)
        print(str(self.client)+" disconnected")


while True:
    client = server.wait_connection()
    thread=recieve_messages(client)
    threads.append(thread)
    threads[len(threads)-1].start()