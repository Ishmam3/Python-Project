from tkinter import *
from time import *

def update():
    time_str = strftime("%I:%M:%S")
    time_label.config(text=time_str)
    
    window.after(1000, update)


window = Tk()

time_label = Label(window,font=("Arial",50), fg="#00ff00", bg="#111111")
time_label.pack()

update()

window.mainloop()