from tkinter import *
from time import *


def update_clock():
    current_time = strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_clock)


window = Tk()

label = Label(window, text="To jest mój pierwszy program", font=("Tahoma", 20))
label.pack()

time_label = Label(window, bg="black", font=("Tahoma", 30), fg="white")
time_label.pack()

update_clock()
window.mainloop()

