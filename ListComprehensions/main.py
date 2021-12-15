fruits = ["jabłko", "banan", "gruszka", "truskawka", "śliwka"]
new_list = []

for f in fruits:
    if "k" in f:
        new_list.append(f)

print(new_list)


new_list2 = [f for f in fruits if "k" in f]
print(new_list2)

print("---------------------------")

numbers = [1, 3, 5, 6, 10]

result = [n * n for n in numbers]
print(result)
