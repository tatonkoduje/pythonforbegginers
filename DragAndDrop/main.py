from tkinter import *


def start_drag(event):
    event.widget.start_x = event.x
    event.widget.start_y = event.y
    drag.set(True)


def stop_drag(event):
    drag.set(False)


def drag_motion(event):
    if drag.get():
        x = event.widget.winfo_x() - event.widget.start_x + event.x
        y = event.widget.winfo_y() - event.widget.start_y + event.y
        event.widget.place(x=x, y=y)


window = Tk()
window.geometry("800x600")

drag = BooleanVar()

box1 = Label(window, width=8, height=4, bg='blue')
box1.place(x=10, y=10)

box2 = Label(window, width=8, height=4, bg='red')
box2.place(x=400, y=300)

box1.bind("<Button-1>", start_drag)
box1.bind("<B1-Motion>", drag_motion)

box2.bind("<Button-1>", start_drag)
box2.bind("<B1-Motion>", drag_motion)

window.mainloop()
