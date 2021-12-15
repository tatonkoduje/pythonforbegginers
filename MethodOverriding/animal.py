class Animal:

    def move(self):
        print("Zwierze porusza się...")

    def make_noise(self):
        print("Zwierze hałasuje!")


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def move(self):
        print(self.name + " biegnie...")

    def make_noise(self):
        print(self.name + " szczeka!")


class Bird(Animal):

    def move(self):
        print("Ptak leci...")

    # def make_noise(self):
    #     print("Ptak ćwierka...")

