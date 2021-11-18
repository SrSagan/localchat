from tkinter import *
from typing import Collection
import server
import concurrent.futures

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
            print("aca estoy")
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
    #print(input_get)
    messages.config(state=NORMAL)
    messages.insert(INSERT, 'Santi: %s\n' % input_get)
    message = server.recv_message()
    messages.insert(INSERT, 'Otro: %s\n' % message)
    messages.config(state=DISABLED)
    server.send_message(str(input_get))
    # label = Label(window, text=input_get)
    input_user.set('')
    # label.pack()
    return "break"

def recived_message():
    message = server.recv_message()
    if(message != b''):
        messages.config(state=NORMAL)
        messages.insert(INSERT, 'Otro: %s\n' % message)
        messages.config(state=DISABLED)
    window.after(0, recived_message)

window.after(0, recived_message)


frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()

window.mainloop()'''
