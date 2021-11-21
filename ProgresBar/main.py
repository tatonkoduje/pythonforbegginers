from tkinter import *
from tkinter.ttk import *
import time


def start_download():
    for i in range(100):
        progress_bar['value'] = i+1
        percent.set(str(i+1) + "%")
        time.sleep(0.05)
        window.update_idletasks()


window = Tk()
window.geometry("600x150")

percent = StringVar()

progress_bar = Progressbar(window, orient=HORIZONTAL, length=400)
progress_bar.pack(pady=20)

percents = Label(window, textvariable=percent).pack(pady=10)
button = Button(window, text="Download", command=start_download)
button.pack()

window.mainloop()
