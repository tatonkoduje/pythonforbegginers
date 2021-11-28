import os

path = "example.txt"
dest = "NowyFolder/example.txt"

try:
    if os.path.exists(dest):
        print("Taki plik już istnieje w docelowej lokalizacji")
    else:
        os.replace(path, dest)
        print("Plik został przeniesiony")
except FileNotFoundError:
    print(path + " nie istnieje")
    