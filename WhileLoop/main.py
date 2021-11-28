counter = 0
while counter < 5:
    print(counter)
    counter += 1

number = 0
while not (5 <= int(number) <= 10):
    number = int(input("Podaj liczbe z przedziału 5-10: "))

print("Brawo. Liczba " + str(number) + " znajduje się w tym przedziale.")

while 1 == 1:
    print("Nieskończona pętla")
