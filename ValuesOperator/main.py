color = "czerwony"
print(color)

print(color := "czerwony")

colors = list()
while True:
    print("Jeśli chcesz wyjść - wpisz 'exit'")
    color = input("Podaj kolor: ")
    if color == "exit":
        break
    colors.append(color)

print(colors)

print("--------------------------------")

names = list()
while (name := input("Podaj imię: ")) != "exit":
    print(name)
    names.append(name)

print(names)
