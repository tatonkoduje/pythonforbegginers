def add(a, b):
    return a + b


print(add(1, 2))


# print(add(1, 2, 3))


def sum_all(*numbers):
    result = 0
    print(numbers)

    for i in numbers:
        result += i
    return result


print(sum_all(1, 2, 3, 4, 10))
print("---------------------------")


def sum_all2(*numbers):
    result = 0
    print(numbers)

    my_list = list(numbers)
    print(my_list)
    my_list[0] = 100

    for i in my_list:
        result += i

    return result


print(sum_all2(2, 3))
