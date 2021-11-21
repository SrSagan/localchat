from tkinter import *
import client
import threading

#TODO el cliente debe conectarse al server y mandar sus mensajes
#en caso de desconectarse debe mandar un codigo de desconeccion
#ademas de eso debe esperar constantemente mensajes del server

client = client.client()

class recieve_messages(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        message = client.recv_message()
        messages.config(state=NORMAL)
        messages.insert(INSERT, "%s\n" % message.decode('utf-8'))
        messages.update()
        messages.config(state=DISABLED)

window = Tk()
label = Label(text="Client")
label.pack()
messages = Text(window)
messages.config(state=DISABLED)
messages.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed(event):
    input_get = input_field.get()
    input_user.set('')

    if(input_get == "/disconnect"):
        client.send_message(str(input_get))
        exit()

    elif("/connect" in input_get):
        x = input_get.find("/connect")
        hostname = input_get[x+9:]
        client.connect(hostname)
        client.set_connected(True)
        print("im here")

    client.send_message(str(input_get))
    return "break"

def recivir_mensajes():
    if(client.get_connected()):
        print("now I'm here")
        recieve_messages().start()
        messages.after(10, recivir_mensajes)

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)

frame.after(10, recivir_mensajes)
frame.pack()
window.mainloop()