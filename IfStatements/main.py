experience = int(input("Od ilu lat programujesz?: "))

if experience <= 0:
    print("To wszystko przed Tobą!")
elif experience == 1:
    print("Dokładnie rok!! Tak trzymaj")
else:
    print("To więcej niz rok!")


if experience < 0 or experience > 100:
    print("To niemożliwe.")
elif experience == 0:
    print("No to czas zacząć")
elif experience > 0 and experience <= 2:
    print("To poziom początkujący")
else:
    print("Brawo, tak trzymaj")


if 0 < experience <= 2:
    print("To poziom początkujący")
elif experience > 3 and not(20 <= experience < 100):
    print("Ponad 3 lata... no no. Ale nie więcej niż 20...")
    