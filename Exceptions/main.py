# a = int(input("Podaj numer: "))
# b = int(input("Podziel ten numer przez: "))
# result = a / b
# print(result)

try:
    a = int(input("Podaj numer: "))
    b = int(input("Podziel ten numer przez: "))
    result = a / b
except ZeroDivisionError:
    print("Nie możesz dzielić przez 0")
except ValueError:
    print("To nie jest liczba!")
except Exception as e:
    print("Coś poszło nie tak")
    print(e)
else:
    print(result)
finally:
    print("Ten blok wykona się zawsze")


class MyError(Exception):
    def __init__(self, **kwargs):
        pass


def input_name():
    name = input("Jak masz na imię? ")
    if name == "Kot":
        raise MyError(message="Takie imię nie istnieje")
    elif name.isdigit():
        raise ValueError
    return name


try:
    my_name = input_name()
except MyError:
    print("To nie jest prawdziwe imię")
except Exception as e:
    print("coś poszło nie tak")
else:
    print(my_name)
