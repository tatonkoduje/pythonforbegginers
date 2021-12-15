from tkinter import *


def create_window():
    window.destroy()
    # new_window = Toplevel()
    new_window = Tk()


window = Tk()
window.geometry("800x600")

button = Button(window, text="Otwórz nowe okno", command=create_window)
button.place(x=200, y=100)

window.mainloop()
