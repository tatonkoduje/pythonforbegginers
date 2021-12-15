colors = ["niebieski", "czerwony", "zielony", "bialy", "zolty", "czarny"]

print(colors[0])
print(colors[2])
print(len(colors))

colors[0] = "rozowy"
print(colors[0])

colors.append("fioletowy")
colors.remove("czerwony")
removed = colors.pop()
print(colors)
print(removed)

colors.insert(1, "pomaranczowy")
print(colors)
colors.sort()
print(colors)
colors.clear()
print(colors)

print("------------------------")

print(colors)
my_colors = colors
my_colors.append("fioletowy")
print(my_colors)
print(colors)

colors.clear()
print(colors)
print(my_colors)

print("-------------------------")

numbers = [2, 5, 7]
my_numbers = numbers.copy()
print(numbers)
numbers.append(0)
my_numbers.append(-1)

print("my_numbers: ", my_numbers)
print("numbers: ", numbers)

print("------------------------")
more_numbers = numbers[:]
more_numbers.append(100)
print("more_numbers: ", more_numbers)
print("numbers: ", numbers)
