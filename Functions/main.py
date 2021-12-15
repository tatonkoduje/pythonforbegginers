def show_name():
    print("Marek")


show_name()
show_name()


def show_full_name():
    print("Marek")
    print("Kowalski")


show_full_name()


def show_person_data(name, surname, age):
    print(name + " " + surname + ", Lat: " + str(age))


show_person_data("Marek", "Kowalski", 18)


def sum_up_to(limit):
    number, result = 0, 0
    while number <= limit:
        result = result + number
        number += 1
    print(result)


sum_up_to(5)

