name = "Darek"


def display_name():
    name = "Marek"
    print(name)


display_name()
print(name)



# LEGB
print("Built-in: ", __name__)

__name__ = "Nasza zmienna"
print("Global: ", __name__)


def outer():
    __name__ = "A"
    print("Enclosing: ", __name__)

    def inner():
        __name__ = "B"
        print("Local: ", __name__)

    inner()


outer()
