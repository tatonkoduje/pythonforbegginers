class Animal:
    def __init__(self, species, name, legs):
        self.species = species
        self.name = name
        self.legs_count = legs

    def run(self):
        print(self.name + " biegnie...")

    def stop(self):
        print(self.name + " zatrzymuje się.")

    def make_noise(self):
        print(self.name + " szczeka!")
