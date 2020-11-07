from tkinter import *
from tkinter import ttk
root=Tk()
Btn1= ttk.Button(root,text="Click1")
Btn1.pack()
Btn2= ttk.Button(root,text="Click2")
Btn2.pack()
Btn3= ttk.Button(root,text="Click3")
Btn3.pack()
def BuClick(x):
    print("Clicked {}".format(x))
#if the function need an argument we have to call lambda
Btn1.config(command=lambda :BuClick(1))
Btn2.config(command=lambda :BuClick(2))
Btn3.config(command=lambda :BuClick(3))

root.mainloop()