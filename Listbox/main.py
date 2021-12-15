from tkinter import *


def select_item():
    # print("Wybrałeś: " + listbox.get(listbox.curselection()))
    selected_cars = [listbox.get(i) for i in listbox.curselection()]
    print("Wybrałeś: " + str(selected_cars))


def add_item():
    if input_text.get() != "":
        listbox.insert(listbox.size(),  input_text.get())
    listbox.config(height=listbox.size())


def delete_item():
    if len(listbox.curselection()) != 0:
        # listbox.delete(listbox.curselection())
        [listbox.delete(i) for i in reversed(listbox.curselection())]
        listbox.config(height=listbox.size())


window = Tk()
window.geometry("800x600")

listbox = Listbox(window)
listbox.config(bg="#FFCCCC",
               font=('Tahoma', 12),
               height=listbox.size(),
               selectmode=MULTIPLE)
listbox.pack()

cars = ["polonez", "fiat126", "trabant", "syrena", "żuk", "duży fiat", "wartburg", "warszawa"]

# listbox.insert(1, "polonez")
# listbox.insert(2, "fiat126")
# listbox.insert(3, "trabant")
# listbox.insert(4, "syrena")
listbox.insert(END, *cars)
listbox.select_set(0)


select_button = Button(window, text="Wybierz", command=select_item)
select_button.pack()

input_text = Entry(window)
input_text.pack()
add_button = Button(window, text='Dodaj', command=add_item)
add_button.pack()

delete_button = Button(window, text="Usuń", command=delete_item)
delete_button.pack()

window.mainloop()
