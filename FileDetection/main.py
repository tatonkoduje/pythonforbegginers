import os

# path = "example.txt"
path = "C:/taton/example2.txt"

print(os.path.exists(path))

if os.path.exists(path):
    print("plik lub folder istnieje...")
    if os.path.isfile(path):
        print("...i jest to plik")
    elif os.path.isdir(path):
        print("...i jest to folder")
else:
    print("Element o podanej ścieżce nie istnieje")

