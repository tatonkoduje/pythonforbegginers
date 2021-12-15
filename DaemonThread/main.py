import threading
import time


def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Program aktywny. ", count)


x = threading.Thread(target=timer, daemon=True)
x.start()
print(x)

input("Chcesz wyjsc?\n")
