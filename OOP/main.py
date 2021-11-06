from animal import Animal


class Person:
    name = "Marek"
    surname = "Kowalski"
    age = 18

    def run(self):
        print(self.name + " biegnie....")


me = Person()
print(me)
me.run()

# animal_1 = Animal()
# animal_1.make_noise()

animal_1 = Animal("dog", "Drops", 3)
print(animal_1.legs_count)
animal_1.run()

animal_2 = Animal("cat", "Miałczek", 4)
print(animal_2.species)
animal_2.run()
