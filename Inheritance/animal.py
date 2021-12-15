class Animal:
    name = "Nieznane"
    legs = 4
    ears = 2

    def __init__(self, name):
        self.name = name

    def move(self):
        print(self.name + " biegnie...")

    def stop(self):
        print(self.name + " zatrzymuje się.")

    def make_noise(self):
        print(self.name + " szczeka!")


class Dog(Animal):
    def run(self):
        print(self.name + " biegnie...")


class Fish(Animal):
    def swim(self):
        print(self.name + " płynie...")


class Bird(Animal):
    def fly(self):
        print(self.name + " leci...")
        