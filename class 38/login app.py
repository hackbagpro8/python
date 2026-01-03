from tkinter import *

window=Tk()
window.title("Login app")
window.geometry('450x500')
window.configure(bg='orange')
def login():
    name1=entry1.get()
    
    g='hello',name1,"\n Welcome to Codingal"+"\n LOgin succesful"
    text1.delete=("1.0",END)
    text1.insert("1.0",g)

frame1=Frame(window,bg='darkorange',bd=3,width=450,height=300,relief='sunken')
frame1.place(x=0,y=0)
label1=Label(frame1,bg='darkorange',text='Name')
label1.place(x=20,y=20)
label2=Label(frame1,bg='darkorange',text='Password')
label2.place(x=20,y=80)
entry1=Entry(frame1)
entry1.place(x=120,y=20)
entry2=Entry(frame1,show='*')
entry2.place(x=120,y=80)
button1=Button(frame1,bg='black',fg='darkorange',text='Login',command=login)
button1.place(x=70,y=120)
text1=Text(window,bg='beige',width=400,height=8,bd=3,relief='sunken')
text1.place(x=0,y=160)

window.mainloop()
