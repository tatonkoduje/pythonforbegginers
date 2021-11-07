class CoffeeMaker:

    def turn_on(self):
        print("Ekspres włącza się...")
        return self

    def turn_off(self):
        print("Ekspres wyłącza się...")
        return self

    def grind(self):
        print("Ekspres mieli ziarno...")
        return self

    def make(self):
        print("Ekspres robi kawe...")
        return self

    def pour(self):
        print("Ekspres nalewa kawe...")
        return self


coffee_maker = CoffeeMaker()
# coffee_maker.turn_on()
# coffee_maker.grind()

coffee_maker.turn_on().grind().make().pour().turn_off()

print('-------------------------------')

coffee_maker.turn_on()\
    .grind()\
    .turn_off()
