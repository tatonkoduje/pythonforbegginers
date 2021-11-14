from tkinter import *

window = Tk()

window.geometry("500x500")
window.title("To jest moje okno")

icon = PhotoImage(file='python.png')
window.iconphoto(True, icon)

window.config(background="#cccccc")
window.maxsize(700, 700)

window.mainloop()
