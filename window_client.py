from tkinter import *
import client

<<<<<<< HEAD
=======
#TODO el cliente debe conectarse al server y mandar sus mensajes
#en caso de desconectarse debe mandar un codigo de desconeccion
#ademas de eso debe esperar constantemente mensajes del server
>>>>>>> 766d6fd3b5865d253493e2b492721a7bbce1d7d2

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
    message = client.recv_message()
    messages.insert(INSERT, 'Otro: %s\n' % message)
    messages.config(state=DISABLED)
    client.send_message(str(input_get))
    input_user.set('')
    return "break"

<<<<<<< HEAD
'''def recived_message():
    message = client.recv_message()
    if(message != b''):
        messages.config(state=NORMAL)
        messages.insert(INSERT, 'Otro: %s\n' % message)
        messages.config(state=DISABLED)
    window.after(0, recived_message)

window.after(0, recived_message)'''
=======
>>>>>>> 766d6fd3b5865d253493e2b492721a7bbce1d7d2

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()
window.mainloop()