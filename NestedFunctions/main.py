def outer_func():
    def inner_func():
        print("Witaj Marku!")

    inner_func()


outer_func()

print("Podaj dane dla równania: y=2x^2+7")
x = input("Podaj wartość x: ")

result = float(x)
result = pow(result, 2)
result = 2 * result
result = result + 7
print(result)


def multiply(value, times):
    return value * times


def add(value, value2):
    return value + value2


print(
    add(
        multiply(
            pow(
                float(
                    input("Ponownie podaj wartość x: ")
                ), 2
            ),
            2
        ),
        7
    )
)

print(add(multiply(pow(float(input("Ponownie podaj wartość x: ")), 2), 2), 7))

print("--------------------------")
print(round(abs(int(-3.14))))
