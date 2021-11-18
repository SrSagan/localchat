from tkinter import *
import client

#TODO el cliente debe conectarse al server y mandar sus mensajes
#en caso de desconectarse debe mandar un codigo de desconeccion
#ademas de eso debe esperar constantemente mensajes del server

client = client.client()

window = Tk()
label = Label(text="Client")
label.pack()
client.connect()
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
    messages.config(state=DISABLED)
    client.send_message(str(input_get))
    input_user.set('')
    return "break"


frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()
window.mainloop()