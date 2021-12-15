counter = 0
while True:
    print(counter)
    counter += 1
    if counter > 5:
        break

print("Przerywam pętle")

for element in range(10):
    if element % 2 == 0:
        continue
    print(element)

print("-----------------------")

names = ["Marek", "Darek", "Arek", "Anka", "Krzysiek", "Dorota", "Andrzej"]
index = 0
search = input("Jakiego imienia szukamy?: ")

while True:
    if index == len(names):
        print("Nic nie znalazłem")
        break

    if names[index].lower() == search.lower():
        print("Znalazłem imię: " + names[index])
        break

    index += 1

print("-----------------------")

for element in range(1, 10):
    if element == 7:
        pass
    else:
        print(element)
