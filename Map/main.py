numbers = [2, 4, 6, 8, 10]


def power(number):
    return number * number


result = map(power, numbers)
print(list(result))

result2 = list(map(lambda number: number * number, numbers))
print(result2)


food = [("chleb", 3),
        ("mleko", 4),
        ("ser", 20),
        ("szynka", 30),
        ("woda", 2)]

inflation = 0.12

prices = list(map(lambda data: (data[0], data[1] + data[1]*inflation), food))
print(prices)

