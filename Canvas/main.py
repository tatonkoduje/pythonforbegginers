from tkinter import *

window = Tk()

canvas = Canvas(window)
canvas.config(height=500, width=500, bg='#CCCCCC')

canvas.create_line(10, 10, 300, 300, fill='green', width=3)
canvas.create_line(10, 500, 300, 10, fill='red', width=3)

canvas.create_rectangle(100, 100, 200, 200, fill='blue')

points = [300, 50, 400, 400, 200, 400]
canvas.create_polygon(points, fill='yellow', outline='pink', width=10)
canvas.pack()

canvas.create_arc(0, 0, 500, 500, fill='brown', style=PIESLICE, start=180, extent=180)

window.mainloop()
