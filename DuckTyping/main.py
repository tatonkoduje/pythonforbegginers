class Child:

    def play(self, toy):
        print("Dziecko ma zabawkę: {}, kolor: {} ".format(toy.name, toy.color))
        toy.move()


class Ball:
    color = "czerwony"
    name = "piłka"

    def move(self):
        print("Piłka się toczy")


class Car:
    color = "niebieski"
    name = "samochodzik"

    def move(self):
        print("Samochodzik jedzie")


ball = Ball()
car = Car()

child = Child()
child.play(ball)
child.play(car)

