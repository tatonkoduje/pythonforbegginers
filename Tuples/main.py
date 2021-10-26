person = ("Marek", "Kowalski", 18, "m", "marek.kowalski@gmail,com", "Marek")

print(person)
print(person.count("Marek"))
print(person.index("m"))
print(person[4])

print("------------------------")

for element in person:
    print(element)
