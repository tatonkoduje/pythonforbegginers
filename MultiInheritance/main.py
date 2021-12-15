from animal import *
from organism import Organism

organism = Organism()
organism.sleep()

print("--------------------")

animal = Animal()
animal.sleep()
animal.move()

print("--------------------")

dog = Dog("Burek")
dog.run()
dog.make_noise()
dog.sleep()
print(dog.alive)
