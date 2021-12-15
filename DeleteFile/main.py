import os
import shutil

path = "example.txt"

try:
    os.remove(path)
    # os.rmdir("NowyFolder")
    # shutil.rmtree("NowyFolder")
except FileNotFoundError:
    print("Plik nie istnieje")
except PermissionError:
    print("Nie masz uprawnień")
except OSError:
    print("Nie możesz tego usunąć za pomocą tej funkcji")
else:
    print(path + " został usunięty")
