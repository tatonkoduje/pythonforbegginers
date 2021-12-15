from tkinter import *


def on_change(event):
    text.set("Wybrana cena to: " + event + " zł")
    # scale.get()


window = Tk()
window.geometry("800x600")


label = Label(window, text="Wyberz cenę")
label.pack()

scale = Scale(window,
              from_=0,
              to=100,
              length=800,
              orient=HORIZONTAL,
              font=('Arial', 8),
              tickinterval=10,
              resolution=1)

scale.config(troughcolor='#DDDDDD',
             fg='#99FFFF',
             bg='#CCCCCC',
             command=on_change)

scale.pack()
scale.set(20)

text = StringVar()
label = Label(window, textvariable=text, font=("Tahoma", 20))
label.pack()

window.mainloop()
