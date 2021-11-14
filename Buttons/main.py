from tkinter import *


def click():
    print("Nacisnąłeś przycisk!")


window = Tk()

button = Button(window, text="Przycisk", command=click)
button.config(font=("Tahoma", 20),
              bg="#cccccc",
              fg="#ffffff",
              activeforeground="#000000",
              activebackground="white")

photo = PhotoImage(file="me.png")

button.config(image=photo, compound='top')
button.pack()

window.mainloop()
