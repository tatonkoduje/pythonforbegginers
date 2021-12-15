class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs


class Dog(Animal):
    def __init__(self, name, legs, ears, tail):
        super().__init__(name, legs)
        # self.name = name
        # self.legs = legs
        self.ears = ears
        self.tail = tail


    def info(self):
        print("{} ma {} nogi, {} uszy. Czy ma ogon?: {}".format(self.name, self.legs, self.ears, self.tail))


class Bird(Animal):
    def __init__(self, name, legs, wings):
        super().__init__(name, legs)
        # self.name = name
        # self.legs = legs
        self.wings = wings

    def info(self):
        print("{} ma {} nogi oraz {} skrzydła.".format(self.name, self.legs, self.wings))


dog = Dog("Burek", 4, 2, True)
bird = Bird("ćwirek", 2, 2)

dog.info()
bird.info()