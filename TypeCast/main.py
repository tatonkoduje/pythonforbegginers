age = 18
height = "180"
weight = 77.3
name = "Marek"

print("Typ zmiennej age:", type(age))
print("Typ zmiennej height:", type(height))
print("Typ zmiennej weight:", type(weight))
print("Typ zmiennej name:", type(name))

height = int(height)
newHeight = height + 20


print("Typ zmiennej height po rzutowaniu:", type(height))
print("Wartość zmiennej newHeight ->", newHeight)
print("Wartość zmiennej newHeight ->" + str(newHeight) + " po sumowaniu")
print("Typ zmiennej newHeight po rzutowaniu:", type(newHeight))


result = age + weight
print(result)
