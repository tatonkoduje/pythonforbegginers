class Child:

    def play(self, toy):
        print("Dziecko ma zabawkę: {}, kolor: {} ".format(toy.name, toy.color))


class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


toy_1 = Toy("piłka", "czerwony")
toy_2 = Toy("samochodzik", "niebieski")

child = Child()
child.play(toy_1)
child.play(toy_2)

print("-----------------------------")


def change_color(toy, color):
    toy.color = color


change_color(toy_1, "czarny")
child.play(toy_1)
