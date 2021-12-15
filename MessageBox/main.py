from tkinter import *
from tkinter import messagebox


def on_click():
     messagebox.showinfo(title="Uwaga !!!",
                         message="To jest kurs dla początkujących.",
                         icon="error")
    # messagebox.showerror(title="Alarm !!!", message="Stało się coś złego !")
    # messagebox.showwarning(title="Uwaga !!!", message="To ostatnie ostrzeżenie !")

    # answer = messagebox.askokcancel(title="Pytanie", message="Jesteś zmęczony ?")
    # if answer:
    #     print("To odpocznij")
    # else:
    #     print("Anulowałeś, czyli jesteś w formie!")

    # answer = messagebox.askretrycancel(title="Pytanie", message="Czy chcesz spróbować jeszcze raz ?")
    # if answer:
    #     print("To próbuj")
    # else:
    #     print("Zrezygnowałeś")

    # messagebox.askyesno(title="Pytanie", message="Jesteś zmęczony ?")
    # answer = messagebox.askyesnocancel(title="Pytanie", message="Jesteś zmęczony ?")
    # if answer:
    #     print("To nie dobrze")
    # elif answer == False:
    #     print("To świetnie!")
    # else:
    #     print("Anulowałeś")

    # answer = messagebox.askquestion(title="Pytanie", message="Jesteś zmęczony ?")
    # if answer == 'yes':
    #     print("To nie dobrze")
    # else:
    #     print("To świetnie!")


window = Tk()
window.geometry("400x200")

button = Button(window, text="Pokaż alert", command=on_click)
button.pack()

window.mainloop()
