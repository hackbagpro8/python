from tkinter import *
window=Tk()
window.title("Main window")
window.geometry("300x300")
window.configure(bg='plum')
def top():
    toplevel1=Toplevel()
    toplevel1.title("Top Level Window")
    toplevel1.geometry('200x200')
    toplevel1.configure(bg='violet')
    label2=Label(toplevel1,text="Top level window")
    label2.pack(pady=2)
    toplevel1.mainloop()


label1=Label(text="Main window")
label1.pack(pady=100)
button1=Button(text="click me",command=top)
button1.pack(pady=10)
window.mainloop()