import threading
import time
import numpy as np


def cycling():
    time.sleep(5)
    print("Jadę na rowerze! ")


def listen_music():
    time.sleep(5)
    print("Słucham muzyki. ")


def drink():
    time.sleep(2)
    print("Pije napój z bidonu. ")


def observe():
    time.sleep(4)
    print("Rozglądam się. ")


time_start = time.perf_counter()

# cycling()
# listen_music()
# drink()
# observe()

cycling_thread = threading.Thread(target=cycling, args=())
cycling_thread.start()

music_thread = threading.Thread(target=listen_music, args=())
music_thread.start()

drink_thread = threading.Thread(target=drink, args=())
drink_thread.start()

observe_thread = threading.Thread(target=observe, args=())
observe_thread.start()


drink_thread.join()
music_thread.join()
cycling_thread.join()
observe_thread.join()


time_stop = time.perf_counter()

print(threading.active_count())
print(threading.enumerate())
print(np.diff([time_start, time_stop]))
