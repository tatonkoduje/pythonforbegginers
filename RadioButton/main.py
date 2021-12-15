from tkinter import *


def choose():
    print("wybrałeś " + cars[button_value.get()])


window = Tk()

cars = ["polonez", "trabant", "fiat126p", "syrena"]
button_value = IntVar()

for index in range(len(cars)):
    radio_button = Radiobutton(window, text=cars[index], variable=button_value, value=index, command=choose)
    radio_button.config(padx=10, font=("Tahoma", 16))
    radio_button.pack(side=LEFT)


window.mainloop()
