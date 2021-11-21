from tkinter import *
from tkinter import colorchooser


def set_button_color():
    color = colorchooser.askcolor()
    print(color)
    button.config(bg=color[1])
    button2.config(bg=color[1])


def set_bg_color():
    window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("400x400")

button = Button(window, text="Wybierz kolor przycisków", command=set_button_color)
button.pack()

button2 = Button(window, text="Wybierz kolor tła", command=set_bg_color)
button2.pack()

window.mainloop()
