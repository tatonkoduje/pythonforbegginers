person = ("Marek", "Kowalski", 18, "m", "marek.kowalski@gmail,com", "Marek")

print(person)
print(person.count("Marek"))
print(person.index("m"))
print(person[4])
print(person[-1])
print(person[2:5])

print("------------------------")

for element in person:
    print(element)

print("------------------------")

tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
tuple3 = tuple1 + tuple2
print(tuple3)

tuple4 = tuple1 * 3
print(tuple4)
