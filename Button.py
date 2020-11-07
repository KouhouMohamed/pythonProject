from tkinter import *
from tkinter import ttk #tkk is a class where buttons



def main():
    root = Tk() #create a root ( a window)
    but1 = ttk.Button(root, text="GetText")

    Ent1 = ttk.Entry(root, width=30)
    Ent1.pack()
    but1.pack()  # Add button to root
    def ButtClick():
        print(Ent1.get()) #get the contenant of Ent1
        Ent1.delete(0,END) #clear the entery from begennin to end
    but1.config(command=ButtClick)
    Logo = PhotoImage(file='help.png')
    Logo_r=Logo.subsample(10,10) #resize the image
    Logo_r.zoom(15,20)
    but1.config(image=Logo_r,compound=LEFT)
    root.mainloop() #pour afficher root




if __name__ == '__main__':main()
