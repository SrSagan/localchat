from tkinter import *
import server

server = server.server()

window = Tk()
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

window.mainloop()