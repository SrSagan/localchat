from tkinter import *
from typing import Collection
import server

server = server.server()

#TODO el server recivira y administrara el resto de clientes
#tiene que estar constantemente esperando conexiones y guardandolas (quiza en una array de clientes)
#si el cliente envia cierto codigo borrarlo de la lista de clientes activos

clients=[]
server.bind()
while True:
    client = server.wait_connection()
    while True:
        clients = server.get_clients()
        message = server.recv_message(client)
        print(message)
        if(message == b"/disconnect"):
            server.disconnect(client)
        else:
            server.send_global(message)
    






























'''window = Tk()
server.bind()
server.wait_connection()

messages = Text(window)
messages.config(state=DISABLED)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    messages.config(state=NORMAL)
    messages.insert(INSERT, 'Santi: %s\n' % input_get)
    messages.config(state=DISABLED)
    server.send_message(str(input_get))
    # label = Label(window, text=input_get)
    input_user.set('')
    # label.pack()
    return "break"

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()'''
