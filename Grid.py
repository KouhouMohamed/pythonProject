from tkinter import *
from tkinter import ttk

root=Tk()
style=ttk.Style()
style.theme_use('classic')

L1=ttk.Label(root,background='Green',text='KOUHOU')
L1.grid(row=0,column=0,sticky='snew')
L2=ttk.Label(root,background='Red',text='Mohamed')
L2.grid(row=0,column=1,sticky='snew')
L3=ttk.Label(root,background='Blue',text='ENSET')
L3.grid(row=1,column=0,columnspan=2,sticky='snew') #snew = south , north, est,west
L4=ttk.Label(root,background='Orange',text='FST')
L4.grid(row=0,column=3,rowspan=2,sticky='snew')

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(3,weight=1)


root.mainloop()