import sys
import tkinter as tk # If this fai

import time

def times():
    current_time = time.strftime("%H : %M : %S")
    clock.config(text=current_time)
    clock.after(200,times)


win = tk.Tk()
win.geometry("500x250")
clock = tk.Label(win,font=("times",50,"bold"),bg="white")
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi = tk.Label(win,text="Digital Clock",font="times 24 bold")
digi.grid(row=0,column=2)

nota = tk.Label(win,text="Hours   Minutes   Seconds    ",font="times 15 bold")
nota.grid(row=3,column=2)

win.mainloop()