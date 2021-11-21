from tkinter import *


def new_project():
    print("Tworzę nowy projekt...")


def open_project():
    print("Otwieram istniejący projekt...")


def save_as():
    print("Zapisuję projekt...")


def edit_command():
    print("Cut, Copy, Paste lub Delete...")


window = Tk()

open_icon = PhotoImage(file="open.png")
copy_icon = PhotoImage(file="copy.png")
cut_icon = PhotoImage(file="cut.png")

menu_bar = Menu(window)
menu_bar.config(bg='#666666')
window.config(menu=menu_bar)

# file menu

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New...", command=new_project, underline=0)
file_menu.add_command(label="Open...", command=open_project, image=open_icon, compound=LEFT)
file_menu.add_command(label="Save As...", command=save_as)

# preferences submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# edit menu

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.config(font=('Arial', 6), fg="#FF0000")
menu_bar.add_cascade(label="File", menu=edit_menu)

edit_menu.add_command(label="Cut", command=edit_command, image=cut_icon, compound=LEFT)
edit_menu.add_command(label="Copy", command=edit_command, image=copy_icon, compound=LEFT)
edit_menu.add_command(label="Paste", command=edit_command)
edit_menu.add_command(label="Delete", command=edit_command)

window.mainloop()
