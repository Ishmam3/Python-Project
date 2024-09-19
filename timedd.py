from tkinter import *
from time import *

def update():
    time_str = strftime("%I:%M:%S")
    time_label.config(text=time_str)
    
    date_str = strftime("%A")
    day_label.config(text=date_str)
    
    date_str = strftime("%B %d, %Y")
    date_label.config(text=date_str)
    window.after(1000, update)


window = Tk()

time_label = Label(window,font=("Arial",50), fg="#00ff00", bg="#111111")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Ink Free", 25))
date_label.pack()

update()

window.mainloop()