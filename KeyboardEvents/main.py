from tkinter import *


def press_key(event):
    print("Nacisnąłeś " + event.keysym)
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>", press_key)

label = Label(window, font=('Tahoma', 40))
label.pack()

window.mainloop()
