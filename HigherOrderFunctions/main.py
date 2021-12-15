def multiply(a, b):
    print("ta funkcja mnoży")
    return a*b


def sum(a, b):
    print("ta funkcja dodaje")
    return a + b


def calculate(a, b, fun):
    return fun(a, b)


def calculate_function():
    return calculate


print("---------------------------")

print(calculate(3, 3, sum))
print(calculate(3, 3, multiply))

my_calculate = calculate
print(my_calculate(4, 4, multiply))

print("---------------------------")

cal = calculate_function()
print(cal(6, 6, multiply))
