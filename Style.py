from tkinter import *
from tkinter import ttk
root=Tk()

B1=ttk.Button(root,text="Button1")
B2=ttk.Button(root,text="Button2")
B3=ttk.Button(root,text="Button3")
B1.pack()
B2.pack()
B3.pack()

style=ttk.Style()
style.theme_use('default')
# make the color of all buttons in blue and backgoun red
style.configure("TButton",foreground='blue',background='red')
style.configure("TButton",font=('Time',18,'bold'))
style.configure("NewClass.TButton",font=('Time',18,'bold'), background='green')
B3.configure(style='NewClass.TButton')
print(style.theme_names(),style.theme_use())


root.mainloop()