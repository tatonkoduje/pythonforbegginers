from organism import Organism


class Animal(Organism):
    name = "Nieznane"

    def move(self):
        print("Zwierzę porusza się...")

    def make_noise(self):
        print(self.name + " hałasuje!")


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name + " biegnie...")

