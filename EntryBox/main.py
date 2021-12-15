from tkinter import *


def submit():
    print("Witaj " + entry_box.get())
    # entry_box.insert(0, "OK")


def clear():
    entry_box.delete(0, END)


def quit():
    window.quit()


window = Tk()

label = Label(window, text="Jak masz na imię?")
label.pack()

entry_box = Entry(window)
entry_box.config(font=("Tahoma", 20),
                 # show="*"
                 )

entry_box.pack()

ok_button = Button(window, text="OK", command=submit, width=15)
ok_button.pack(side=LEFT)

clear_button = Button(window, text="Clear", command=clear, width=15)
clear_button.pack(side=RIGHT)

quit_button = Button(window, text="Quit", command=quit, width=15)
quit_button.pack()

window.mainloop()
