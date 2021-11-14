from tkinter import *


def agree():
    if checkbox_value.get() is True:
        print("Zgodziłes się")
        checkbox.config(fg='#000000', bd=0)
        info_label.pack_forget()
    else:
        print("Nie zgadzasz się")
        checkbox.config(fg='#FF0000', relief=SOLID, bd=1)
        info_label.pack(side=LEFT)


window = Tk()
window.geometry("400x100")

checkbox_value = BooleanVar()

checkbox = Checkbutton(window, text="Wyrażam zgodę na wykorzystanie mojego wizerunku w internecie!", command=agree)
checkbox.config(variable=checkbox_value,
                onvalue=True,
                offvalue=False)
checkbox.pack()

info_label = Label(window,
                   text="Musisz wyrazić zgodę!",
                   padx=15,
                   font=("Tahoma", 15))

window.mainloop()
