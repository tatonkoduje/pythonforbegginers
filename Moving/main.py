from tkinter import *

speed = 10
window = Tk()
window.geometry("800x600")
starship = PhotoImage(file="starship.png")


def press_key(event):
    match event.keysym:
        case "w":
            container.place(x=container.winfo_x(), y=container.winfo_y()-speed)
        case "s":
            container.place(x=container.winfo_x(), y=container.winfo_y()+speed)
        case "d":
            container.place(x=container.winfo_x()+speed, y=container.winfo_y())
        case "a":
            container.place(x=container.winfo_x()-speed)


container = Label(window, image=starship)
container.place(x=0, y=0)

window.bind("<w>", press_key)
window.bind("<s>", press_key)
window.bind("<d>", press_key)
window.bind("<a>", press_key)

# =================================================================================


def press_key(event):
    match event.keysym:
        case "Up":
            container2.move(image, 0, -speed)
        case "Down":
            container2.move(image, 0, speed)
        case "Right":
            container2.move(image, speed, 0)
        case "Left":
            container2.move(image, -speed, 0)


container2 = Canvas(window, width=400, height=600, bg="grey")
container2.place(x=400)

image = container2.create_image(0, 0, image=starship, anchor=NW)

window.bind("<Up>", press_key)
window.bind("<Down>", press_key)
window.bind("<Right>", press_key)
window.bind("<Left>", press_key)

window.mainloop()
