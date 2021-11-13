prizes = {"mleko": 2, "chleb": 4, "szynka": 30, "ser": 20, "woda": 2}

prizes_in_euro = {key: (value * 4.4) for (key, value) in prizes.items()}
print(prizes_in_euro)

selected_items = {key: value for (key, value) in prizes_in_euro.items() if value > 10}
print(selected_items)

next_items = {key: (float(round(value)) if value < 20 else int(value)) for (key, value) in selected_items.items()}
print(next_items)

print('---------------------')

cars = {"polonez": "czerwony", "trabant": "czarny", "fiat126p": "biały", "syrenka": "niebieska", "żuk": "czarny"}

"""def change_color(color):
    if color == "czarny":
        return "różowy"
    else:
        return color"""

# painted_cars = {key: (change_color(value)) for (key, value) in cars.items()}
lambda_change_color = lambda color: "różowy" if (color == "czarny") else color

painted_cars = {key: (lambda_change_color(value)) for (key, value) in cars.items()}
print(painted_cars)
