from tkinter import *
from datetime import date,datetime

root=Tk()
root.title("number pad")
root.geometry("200x300")
root.configure(bg='skyblue')
t=[[7,8,9],[4,5,6],[1,2,3],['0','#','*']]
for i in range(0,4):
    root.rowconfigure(i,weight=0 , minsize=80)
    for j in range(0,3):
        root.columnconfigure(i,weight=1,minsize=70)
        label1=Label(root,text=t[i][j],width=3,bg='navy',fg='white',bd=3,relief='sunken')
        label1.grid(row=i,column=j)



root.mainloop
