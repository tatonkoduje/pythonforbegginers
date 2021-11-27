from tkinter import *
import time

WIDTH = 800
HEIGHT = 600
speedX = 5
speedY = 5

window = Tk()
window.geometry("800x600")

canvas = Canvas(window, width=WIDTH, height=600)
canvas.pack()

starship = PhotoImage(file="starship.png")
container = canvas.create_image(0, 0, image=starship, anchor=NW)
container_height = starship.height()
container_width = starship.width()

while True:
    position = canvas.coords(container)

    print(position)

    if position[0] >= WIDTH - container_width or position[0] < 0:
        speedX = -speedX

    if position[1] >= HEIGHT - container_height or position[1] < 0:
        speedY = -speedY

    canvas.move(container, speedX, speedY)
    window.update()
    time.sleep(0.01)


window.mainloop()
