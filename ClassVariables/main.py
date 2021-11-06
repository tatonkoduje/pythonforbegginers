from animal import Animal


animal_1 = Animal("dog", "Drops", 3)
animal_2 = Animal("cat", "Miałczek", 4)

print(Animal.ears)
print("animal 1 ears: ", animal_1.ears)
print("animal 2 ears: ", animal_2.ears)

animal_2.legs_count = 8
print("animal 2 legs: ", animal_2.legs_count)

Animal.name = "nowe imię"
print("animal 1 legs: ", animal_1.name)
print("animal 2 legs: ", animal_2.name)

Animal.ears = 7
print("animal 1 ears: ", animal_1.ears)
print("animal 2 ears: ", animal_2.ears)
