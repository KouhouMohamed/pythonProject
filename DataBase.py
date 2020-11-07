from tkinter import *
from tkinter import ttk
import sqlite3

def main():
    root = Tk()
    style = ttk.Style()
    style.theme_use('classic')
    db=sqlite3.connect("MyData.db")
    db.execute("create table if not exists Admin (Name text,Age int)")
    db.row_factory = sqlite3.Row
    label1 = ttk.Label(root, text="Name", backgroun='red')
    label1.grid(row=0, column=0, sticky='snew')
    entry1 = ttk.Entry(root, width=30)
    entry1.grid(row =0, column= 1, columnspan=5)

    label2 = ttk.Label(root, text="Age", backgroun='red')
    label2.grid(row=1, column=0, sticky='snew')
    entry2 = ttk.Entry(root, width=30)
    entry2.grid(row=1, column=1, columnspan=5)
    style.configure("TEntry",foreground = 'Green')
    btn =ttk.Button(root,text="Add")
    btn.grid(row=4,column=3,columnspan=5)
    B= ttk.Button(root, text="Check")
    B.grid(row=5, column=0, sticky='snew')
    entry3 = ttk.Entry(root, width=30)
    entry3.grid(row=5, column=1, columnspan=5)

    def GetData():
        db.execute("INSERT INTO Admin VALUES (?,?)", (entry1.get(), entry2.get()))
        db.commit()
        entry1.delete(0,END)
        entry2.delete(0, END)

    def Check():
        age = int(entry3.get())
        row = db.execute("select * from Admin")
        for r in row:
            if r['Age'] == age:
                print(r['Name'])

    btn.config(command= GetData)
    B.config(command=Check)


    root.mainloop()



if __name__ == '__main__':main()
