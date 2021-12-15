import time
from multiprocessing import Process, cpu_count
import numpy as np


def counter(limit):
    count = 1
    while count < limit:
        count += 1

    print(count)


def main():
    print(cpu_count())

    start_time = time.time()

    a = Process(target=counter, args=(125000000,))
    b = Process(target=counter, args=(125000000,))
    c = Process(target=counter, args=(125000000,))
    d = Process(target=counter, args=(125000000,))
    e = Process(target=counter, args=(125000000,))
    f = Process(target=counter, args=(125000000,))
    g = Process(target=counter, args=(125000000,))
    h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    e.start()
    f.start()
    g.start()
    h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    e.join()
    f.join()
    g.join()
    h.join()

    stop_time = time.time()
    print("Koniec w czasie: ", np.diff([start_time, stop_time]))


if __name__ == '__main__':
    main()
