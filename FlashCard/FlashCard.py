from tkinter import *

import random
import pandas


BACKGROUND_COLOR = "#B1DDC6"

data=pandas.read_csv("E:\PYTHON\FlashCard\English_nep_spreadsheet.csv")
data_dict=data.to_dict(orient="Records")


windows=Tk()
windows.title("Flash Card")
windows.minsize(width=1000, height=700)
windows.config(bg=BACKGROUND_COLOR)
windows.grid()
card={}

def nextCard():
    global card, flip_timer
    windows.after_cancel(flip_timer)
    card=random.choice(data_dict)
    canvas.itemconfig(ti,text="Nepali", fill="black")
    canvas.itemconfig(fw,text=card["Nepali"], fill="black")
    canvas.itemconfig(background, image=front)
    flip_timer=windows.after(4000, func=flipCard)

def flipCard():
    canvas.itemconfig(ti, text="English", fill="white")
    canvas.itemconfig(fw, text=card["English"], fill="white")
    canvas.itemconfig(background, image=back)
    
    
flip_timer=windows.after(4000, func=flipCard)    
    
canvas=Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)

front=PhotoImage(file="E:\PYTHON\FlashCard\card_front.png")
back=PhotoImage(file="E:\PYTHON\FlashCard\card_back.png")
background=canvas.create_image(500,350, image=front)
ti=canvas.create_text(500,200,text="Title", font=("Ariel", 40, "italic" ))
fw=canvas.create_text(500,380,text="Word", font=("Ariel", 60, "bold" ))
canvas.grid(row= 1, column= 1, columnspan=2, padx=20, pady=20)


right=PhotoImage(file="E:\PYTHON\FlashCard\wright.png")
rightb=Button(image=right)
rightb.config(highlightthickness=0, padx=20, pady=20, command=nextCard)
rightb.grid(row= 2, column= 1)


wrong=PhotoImage(file="E:\PYTHON\FlashCard\wrong.png")
wrongb=Button(image=wrong)
wrongb.config(highlightthickness=0, padx=20, pady=20, command=nextCard)
wrongb.grid(row= 2, column= 2)

nextCard()

windows.mainloop()