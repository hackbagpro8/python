from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

root=Tk()
root.title("Denimation calculator")
root.geometry('600x600')
upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
img=ImageTk.PhotoImage(upload)

label=Label(root,image=img)

label.place(x=100,y=20)

Label1=Label(root,text="hey use welcome to denominator calculator")
Label1.place(x=20,y=320)

def msg():
    msgbox=messagebox.showinfo('alert',"do you want to calculate the denomination count ?")
    if msgbox=='ok':
        topwin()
button1=Button(root,text="Letsa get started!",command=msg,bg='brown',fg='white')
button1.place(x=180,y=380)

def topwin():
    def calulator():
        global amount
        amount=int(entry1.get())
        note2000=amount//2000
        note500=(amount%2000)//500
        note100=((amount%2000)%500)//100
        t1.insert(END,str(note2000))
        t2.insert(END,str(note500))
        t3.insert(END,str(note100))
    top=Toplevel()
    top.title("top level")
    top.geometry("400x400")
    label=Label(top,text="enter total amount")
    label.place(x=80,y=100)
    entry1=Entry(top)
    entry1.place(x=180,y=100)
    lb1 =Label(top,text="here are the number of notes for each")
    lb1.place(x=50,y=150)
    l1=Label(top,text="2000")
    l2=Label(top,text="500")
    l3=Label(top,text="100")
    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)
    btn=Button(top,text='calculate',command=calulator)
    btn.place(x=150,y=120)
    l1.place(x=100,y=200)
    l2.place(x=100,y=230)
    l3.place(x=100,y=250)
    t1.place(x=200,y=200)
    t2.place(x=200,y=230)
    t3.place(x=200,y=250)

root.mainloop()
