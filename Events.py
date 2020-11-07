from tkinter import *
from tkinter import ttk
root=Tk()

def Key_Press(event):
    print("type {}".format(event.type))
    print("Key Pressed")
def Butt_Press(event):
    print("type {}".format(event.type))
    print("Button Pressed")

but=ttk.Button(root,text='Click me')
but.pack()
but.bind('<ButtonPress>',Butt_Press)
root.bind("<Control-c>",Key_Press) #if we press Crtl C we call the function
root.mainloop()
