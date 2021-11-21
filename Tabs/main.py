from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("800x600")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="Zakładka 1")
notebook.add(tab2, text="Zakładka 2")
notebook.pack(expand=True, fill="both")

Label(tab1, text="To jest tab nr 1", font=('Tahoma', 40)).pack()
Label(tab2, text="To jest tab nr 2", font=('Tahoma', 40), fg="#FF0000").pack()

window.mainloop()
