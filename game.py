from tkinter import *
from tkinter.ttk import Progressbar
from tkcalendar import *
from datetime import timedelta
from datetime import datetime
import random

i = 0

def calc():
    global i
    value = random.choices(
     population=[0   , 100  , 1000 , 2000 , 3000 , 5000 , -100 , -1000, -2000, -3000, -5000, -i  ],
     weights=   [0.03 , 0.18  , 0.14 , 0.09 , 0.05 , 0.01 , 0.18 , 0.14 , 0.09 ,  0.05, 0.01 , 0.03],
     k=1)
    i = i+value[0]
    print(i)
    lbl_value["text"] = i
    now = datetime.now()
    print("now =", now)



window = Tk()
window.title("Game")
window.configure(background='#FFFFFF')
window.geometry('400x250')

title_text = Label(text="THE GAME",bg='#FFFFFF', fg='#000000',font=("Arial", 15,'bold'))
title_text.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.09)

botao = Button(text='      ',command=calc,bg='blue')
botao.place(relx=0.0166,rely=0.15, relwidth = 0.18, relheight = 0.11)

botao = Button(text='      ',command=calc,bg='red')
botao.place(relx=0.2132,rely=0.15, relwidth = 0.18, relheight = 0.11)

botao = Button(text='      ',command=calc,bg='yellow')
botao.place(relx=0.4098,rely=0.15, relwidth = 0.18, relheight = 0.11)

botao = Button(text='      ',command=calc,bg='brown')
botao.place(relx=0.6064,rely=0.15, relwidth = 0.18, relheight = 0.11)

botao = Button(text='EMPRESTAR',command=calc,bg='orange')
botao.place(relx=0.803,rely=0.15, relwidth = 0.18, relheight = 0.11)

lbl_value = Label(text="0",bg='white',height=50, width=50)
lbl_value.place(relx=0.2,rely=0.3, relwidth = 0.96, relheight = 0.11)

window.mainloop()