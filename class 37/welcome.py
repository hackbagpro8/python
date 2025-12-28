from tkinter import *
from datetime import date,datetime
window=Tk()

window.title("Welcome application")
window.geometry('400x300')
window.configure(bg='orange')
def greet():
    g=entry1.get()
    dt=datetime.now()
    w="walcome to landous "+g+"\n Today date is" + str(dt)
    text1.delete=("1.0","end")
    text1.insert("1.0",w)

label1=Label(text="Name:",fg="green",bg='darkorange')
label1.pack(pady=10)
entry1=Entry()
entry1.pack(pady=10)
button1= Button(text="start",fg='brown',bg='red',command=greet)
button1.pack(pady=10)
text1= Text(bg='darkgrey',fg='white',width=300,height=10,relief='sunken',bd=4)
text1.pack(pady=10)
