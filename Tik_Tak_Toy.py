# -*-coding:Latin-1 -*
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint  # to play with the computer
from time import *
from threading import Thread


ActivePlayer = 1
P1 = []
P2 = []
NbrButClick = 0

root = Tk()
root.title("KOUHOU : Tik Tak Toy")
style = ttk.Style()
style.theme_use('classic')
style.configure("TButton", font=('Time', 18, 'bold'), background='red')

menubar = Menu(root)
setmenu = Menu(menubar, tearoff=0)

setmenu.add_cascade(label="orange", command=lambda: affiche("orange", "blue"))
setmenu.add_cascade(label="red", command=lambda: affiche("red", "orange"))
setmenu.add_cascade(label="green", command=lambda: affiche("green", "yellow"))
setmenu.add_cascade(label="blue", command=lambda: affiche("blue", "green"))
setmenu.add_cascade(label="yellow", command=lambda: affiche("yellow", "red"))
setmenu.add_cascade(label="black", command=lambda: affiche("black", "white"))


def affiche(color,bcolor):
    style.configure("TLabel", background=color)
    style.configure("TButton", background=color)
    style.configure("info.TButton", background=bcolor)


menubar.add_cascade(label="SetColor", menu=setmenu)
root.config(menu=menubar)

label = ttk.Label()
label.grid(row=6, column=0, columnspan=3, sticky='snew', ipadx=40, ipady=15)
style.configure("TLabel", background='red', font=("Time", 18, ''))

F1 = ttk.Frame(root)
F1.grid(row=0, column=0, columnspan=3)
F1.config(width=200, height=200)

L = ttk.Label(F1, text='Choose your mode')
L.grid(row=0, column=0, sticky='snew', ipadx=40)
# Pour choisir le mode de jeu
B1 = ttk.Radiobutton(F1, text='Autopaly  ')
B1.grid()
B2 = ttk.Radiobutton(F1, text='WithFriend')
B2.grid()

modeChoose = StringVar()
modeChoose.set('Autoplay')

B1.config(variable=modeChoose, value='Autoplay')
B2.config(variable=modeChoose, value='WithFriend')

b1 = ttk.Button()
b1.grid(row=3, column=0, sticky='snew', ipadx=40, ipady=40)
b1.config(command=lambda: buclick(1))

b2 = ttk.Button()
b2.grid(row=3, column=1, sticky='snew', ipadx=40, ipady=40)
b2.config(command=lambda: buclick(2))

b3 = ttk.Button()
b3.grid(row=3, column=2, sticky='snew', ipadx=40, ipady=40)
b3.config(command=lambda: buclick(3))

b4 = ttk.Button()
b4.grid(row=4, column=0, sticky='snew', ipadx=40, ipady=40)
b4.config(command=lambda: buclick(4))

b5 = ttk.Button()
b5.grid(row=4, column=1, sticky='snew', ipadx=40, ipady=40)
b5.config(command=lambda: buclick(5))

b6 = ttk.Button()
b6.grid(row=4, column=2, sticky='snew', ipadx=40, ipady=40)
b6.config(command=lambda: buclick(6))

b7 = ttk.Button()
b7.grid(row=5, column=0, sticky='snew', ipadx=40, ipady=40)
b7.config(command=lambda: buclick(7))

b8 = ttk.Button()
b8.grid(row=5, column=1, sticky='snew', ipadx=40, ipady=40)
b8.config(command=lambda: buclick(8))

b9 = ttk.Button()
b9.grid(row=5, column=2, sticky='snew', ipadx=40, ipady=40)
b9.config(command=lambda: buclick(9))

label = ttk.Label(text=strftime("%A %d %B %Y".center(35)))
label.grid(row=6, column=0, columnspan=3, sticky='snew', ipadx=40, ipady=15)
style.configure("TLabel", background='red', font=("Time", 18,'bold'))

ButReplay = ttk.Button(text='Repaly')
ButReplay.grid(row=7, column=0, columnspan=3, sticky='snew', ipadx=40, ipady=15)
style.configure("info.TButton", background='Orange', font=("Time", 18))
ButReplay.configure(style="info.TButton")


def Replay():
    global NbrButClick
    global P1, P2
    global ActivePlayer
    global b1, b2, b3, b4, b5, b6, b7, b8, b9


    NbrButClick = 0
    P1 = []
    P2 = []
    ActivePlayer = 1
    b1.state(['!disabled'])
    b2.state(['!disabled'])
    b3.state(['!disabled'])
    b4.state(['!disabled'])
    b5.state(['!disabled'])
    b6.state(['!disabled'])
    b7.state(['!disabled'])
    b8.state(['!disabled'])
    b9.state(['!disabled'])

    b1.config(text='')
    b2.config(text='')
    b3.config(text='')
    b4.config(text='')
    b5.config(text='')
    b6.config(text='')
    b7.config(text='')
    b8.config(text='')
    b9.config(text='')


ButReplay.config(command=Replay)
# Si on met ces deux instructions en commentaire le palyer peut changer le mode et continuer le jeu
B1.config(command=Replay)
B2.config(command=Replay)


def buclick(id):
    global ActivePlayer
    global P1, P2
    global NbrButClick, modeChoose
    NbrButClick += 1
    if ActivePlayer == 1:
        set_layout(id, "X")
        P1.append(id)
        root.title("KOUHOU : Tik Tak Toy (Player 2)")
        ActivePlayer = 2
        check_winner(NbrButClick)
        if NbrButClick != 0:
            if modeChoose.get() == 'Autoplay':  # choisir le mode de jeu
                auto_play()
    else:
        set_layout(id, "O")
        P2.append(id)
        root.title("KOUHOU : Tik Tak Toy (Player 1)")
        ActivePlayer = 1
        check_winner(NbrButClick)


def set_layout(id, titel):
    if id == 1:
        b1.config(text=titel)
        b1.state(['disabled'])

    elif id == 2:
        b2.config(text=titel)
        b2.state(['disabled'])

    elif id == 3:
        b3.config(text=titel)
        b3.state(['disabled'])

    elif id == 4:
        b4.config(text=titel)
        b4.state(['disabled'])

    elif id == 5:
        b5.config(text=titel)
        b5.state(['disabled'])

    elif id == 6:
        b6.config(text=titel)
        b6.state(['disabled'])

    elif id == 7:
        b7.config(text=titel)
        b7.state(['disabled'])

    elif id == 8:
        b8.config(text=titel)
        b8.state(['disabled'])

    elif id == 9:
        b9.config(text=titel)
        b9.state(['disabled'])


def check_winner(N):
    winner = -1
    if (1 in P1) and (2 in P1) and (3 in P1):
        winner = 1
    if (1 in P2) and (2 in P2) and (3 in P2):
        winner = 2

    if (4 in P1) and (5 in P1) and (6 in P1):
        winner = 1
    if (4 in P2) and (5 in P2) and (6 in P2):
        winner = 2

    if (7 in P1) and (8 in P1) and (9 in P1):
        winner = 1
    if (7 in P2) and (8 in P2) and (9 in P2):
        winner = 2

    if (1 in P1) and (4 in P1) and (7 in P1):
        winner = 1
    if (1 in P2) and (4 in P2) and (7 in P2):
        winner = 2

    if (2 in P1) and (5 in P1) and (8 in P1):
        winner = 1
    if (2 in P2) and (5 in P2) and (8 in P2):
        winner = 2

    if (9 in P1) and (6 in P1) and (3 in P1):
        winner = 1
    if (9 in P2) and (6 in P2) and (3 in P2):
        winner = 2

    if (1 in P1) and (5 in P1) and (9 in P1):
        winner = 1
    if (1 in P2) and (5 in P2) and (9 in P2):
        winner = 2

    if (7 in P1) and (5 in P1) and (3 in P1):
        winner = 1
    if (7 in P2) and (5 in P2) and (3 in P2):
        winner = 2

    if winner == 1:
        messagebox.showinfo(title='Cong', message="Player 1 is the Winner")
        Replay()
    elif winner == 2:
        messagebox.showinfo(title='Cong', message="Player 2 is the Winner")
        Replay()
    if N == 9 and winner == -1:
        messagebox.showerror(title='Game Over', message='Game is over and no one wins')
        Replay()


def auto_play():
    global P1,P2
    global ActivePlayer

    empty_cell = []
    for cell in range(9):
        if not ((cell + 1 in P1) or (cell + 1) in P2):
            empty_cell.append(cell + 1)

    rand_index = randint(0, len(empty_cell) - 1)
    buclick(empty_cell[rand_index])
    ActivePlayer = 1


class Time(Thread):

    def run(self):
        global label
        while 1:
            label.config(text=strftime("%A %d %B %Y %H:%M:%S").center(50))
            sleep(1)


Thread1 = Time()
Thread1.start()

root.mainloop()
Thread1.join()