from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("To moje pierwsze okno")

photo = PhotoImage(file='me.png')

label = Label(window,
              text="Marek Kowalski",
              font=("Impact", 15, "italic"),
              fg="red",
              bg="#cccccc",
              image=photo,
              compound='bottom')


# label.pack()
label.config(fg="#000000",
             relief=SOLID,
             bd=2,
             padx=40,
             pady=40)


label.place(x=20, y=20)

window.mainloop()
