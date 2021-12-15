from tkinter import *


def login():
    print("Username: ", username_entry.get())
    print("Hasło: ", password_entry.get())


window = Tk()

window.geometry("240x100")
window.title('Login')
window.resizable(0, 0)

# configure the grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


# username
username_label = Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

username_entry = Entry(window)
username_entry.grid(column=1, row=0, sticky=E, padx=5, pady=5)

# password
password_label = Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

password_entry = Entry(window,  show="*")
password_entry.grid(column=1, row=1, sticky=E, padx=5, pady=5)

# login button
login_button = Button(window, text="Login", command=login)
login_button.grid(column=1, row=3, sticky=E, padx=5, pady=5)


window.mainloop()
