from tkinter import *


def on_mouse_event(event):
    print(event)
    label.config(text="x={}, y={}".format(str(event.x), str(event.y)))


window = Tk()
window.geometry("400x300")

window.bind("<Button-1>", on_mouse_event)  # left  mouse button
window.bind("<Button-2>", on_mouse_event)  # middle button
window.bind("<Button-3>", on_mouse_event)  # right button
window.bind("<Button-4>", on_mouse_event)  # right button
window.bind("<Button-5>", on_mouse_event)  # right button

# window.bind("<Button>", on_mouse_event)  # any button
# window.bind("<ButtonRelease>", on_mouse_event)  # release any button
# window.bind("<Enter>", on_mouse_event)  # mouse over window
# window.bind("<Leave>", on_mouse_event)  # mouse left window
# window.bind("<Motion>", on_mouse_event)  # mouse move

label = Label(window, font=('Tahoma', 40))
label.pack()

window.mainloop()
