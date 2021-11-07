def power(x, y):
    return x ** y


print(power(3, 3))

power_lambda = lambda x, y: x ** y
multiply = lambda x, y: x * y

print(power_lambda(2, 3))
print(multiply(2, 3))

check_positive = lambda value: True if value >= 0 else False
print(check_positive(1))


class Player:
    def __init__(self, name):
        self.name = name


new_player = Player("Arek")
my_key = lambda player: player.name
print(my_key(new_player))

players = [Player("Marek"), Player("Bartek"), Player("Marian"), Player("Darek"), Player("Zbychu")]
# result = sorted(players, key=my_key)
result = sorted(players, key=lambda player: player.name)

print("--------------------------")
for p in result:
    print(p.name)
