from ctypes import addressof
import server
import threading

server = server.server()

#TODO comentar todo no se entiende un pingo ke esta pasando en ningun lado

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

            #decode message and adress
            x = message.find("/-/")
            adress = message[x+3:]
            message = message[:x]
            print("adress:", adress)
            print("message:", message)


            if(message == "/disconnect"):
                message = adress+" disconnected"
                server.send_event(message)
                server.disconnect(self.client)
                break

            elif("/name" in message):
                x = message.find("/name")
                if(x == 0):
                    name = message[x+6:]
                    server.add_name(name)
                    server.add_host(adress)
            else:
                server.send_global(message, adress)
        print(str(self.client)+" disconnected")


while True:
    client = server.wait_connection()
    thread=recieve_messages(client)
    threads.append(thread)
    threads[len(threads)-1].start()