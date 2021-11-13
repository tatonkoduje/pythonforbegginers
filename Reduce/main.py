from functools import reduce

numbers = [2, 4, 1, 3, 10]

result = reduce(lambda a, b: a + b, numbers)
print(result)
