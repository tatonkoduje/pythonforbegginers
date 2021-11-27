path = "example.txt"

new_text = "To jest nowy tekst, który został wpisany do pliku z programu.\nI nadpisał poprzednią zawartość!!!\n"
new_text2 = "To jest nowy tekst, który został wpisany do pliku z programu.\nI został dopisany bez usuwania poprzedniego.\n"

try:
    with open(path, 'w', encoding='utf-8') as file:
        file.write(new_text)
except FileNotFoundError:
    print("Nie ma takiego pliku")
