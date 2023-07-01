from tkinter import *
from PIL import Image, ImageTk
import random

def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    i.configure(image=DiceImage)
    i.image = DiceImage

    

u=Tk()
u.title("dice simulator")
u.geometry("400x750")
u.config(bg="cyan")


f1=Frame(u,bg="red",borderwidth=15,relief=RAISED)
f1.pack(anchor="n",pady=10)

t=Label(f1,text="Welcome to Dice Simulator",bg="orange",font=("comicsansms",20,"bold",))
t.pack(side="top")

dice = [ 'F:\c++\dice simulator\die1.png','F:\c++\dice simulator\die2.png', 'F:\c++\dice simulator\die3.png', 'F:\c++\dice simulator\die4.png', 'F:\c++\dice simulator\die5.png', 'F:\c++\dice simulator\die6.png']
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

i=Label(u,image=DiceImage)
i.pack(anchor="s",pady=59)

f2=Frame(u,bg="grey",borderwidth=8,relief=SUNKEN)
f2.pack(side="bottom",pady=20)

b=Button(f2,text="Click to Roll Dice",font=("arial",12,"bold"),command=rolling_dice)
b.pack()


u.mainloop()


