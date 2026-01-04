from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Alert system")
window.geometry('300x300')
window.configure(bg='orange')

def scan(event):
    messagebox.showwarning("alert","virus found")

button1 = Button(text="Scan for Virus")
button1.bind("<Button-1>",scan)
button1.pack(pady=70)

window.mainloop()