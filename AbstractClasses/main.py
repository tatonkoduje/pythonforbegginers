from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_noise(self):
        pass


class Dog(Animal):
    def make_noise(self):
        print("Pies szczeka")

    def move(self):
        print("Pies biega")



class Bird(Animal):
    def make_noise(self):
        print("Ptak ćwierka")

    def move(self):
        print("Ptak lata")


#animal = Animal()
#print(animal)
#animal.move()

dog = Dog()
dog.move()
dog.make_noise()

bird = Bird()
bird.move()
bird.make_noise()
