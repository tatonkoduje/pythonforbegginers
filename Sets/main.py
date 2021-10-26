colors = {"czerwony", "niebieski", "zolty", "zielony"}

colors.add("czarny")
colors.remove("czerwony")
#colors.clear()
print(len(colors))

for element in colors:
    print(element)

print("--------------------")

set1 = {1, 2, 3}
set2 = set(("a", "b", "c"))

set1.update(set2)
print(set1)
print(type(set))

my_set = set1.union(set2)
print(my_set)

print("--------------------")

new_set1 = {1, "a", 100}
new_set2 = {200, 3, "a"}
print(new_set1.difference(new_set2))
print(new_set1.intersection(new_set2))
