from tkinter import *


window = Tk()
window.geometry("800x600")

frame = Frame(window, bg='#CCCCCC')
frame.pack(side=TOP)

Button(frame, text="1", font=('Tahoma', 25), width=3).pack(side=TOP)
Button(frame, text="2", font=('Tahoma', 25), width=3).pack(side=LEFT)
Button(frame, text="3", font=('Tahoma', 25), width=3).pack(side=LEFT)
Button(frame, text="4", font=('Tahoma', 25), width=3).pack(side=LEFT)


frame = Frame(window, bg='#CCCCCC')
frame.place(x=700, y=200)
Button(frame, text="5", font=('Tahoma', 25), width=3).pack(side=TOP)
Button(frame, text="6", font=('Tahoma', 25), width=3).pack(side=TOP)
Button(frame, text="7", font=('Tahoma', 25), width=3).pack(side=TOP)

window.mainloop()
