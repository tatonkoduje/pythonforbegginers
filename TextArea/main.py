from tkinter import *


def submit():
    print(text.get('1.0', END))


window = Tk()
window.geometry("800x600")
window.config(bg='#333333')

text = Text(window)
text.config(bg='#000000',
            font=('Courier', 10, 'bold'),
            fg='#78f542',
            height=30,
            width=90,
            padx=5,
            pady=5)
text.pack()

button = Button(window, text="Wyślij", command=submit)
button.pack()

window.mainloop()
