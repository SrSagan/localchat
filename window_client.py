from tkinter import *
import client


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
    # label = Label(window, text=input_get)
    input_user.set('')
    # label.pack()
    return "break"

'''def recived_message():
    message = client.recv_message()
    if(message != b''):
        messages.config(state=NORMAL)
        messages.insert(INSERT, 'Otro: %s\n' % message)
        messages.config(state=DISABLED)
    window.after(0, recived_message)

window.after(0, recived_message)'''

frame = Frame(window)  # , width=300, height=300)
input_field.bind("<Return>", Enter_pressed)
frame.pack()
window.mainloop()