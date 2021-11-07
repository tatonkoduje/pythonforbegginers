def hello():
    print("Hello!")


print(hello)

hi = hello
print(hi)

hi()
hello()


def multiply(a, b):
    print("Ta funkcja mnoży")
    return a*b


print(multiply(2, 2))

my_multiply = multiply
my_multiply(3, 3)
