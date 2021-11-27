path = "example.txt"

try:
    with open(path, encoding='utf-8') as file:
        print(file)
        print(file.read())
except FileNotFoundError:
    print("Nie ma takiego pliku")
