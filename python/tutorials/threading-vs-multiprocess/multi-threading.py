from threading import Thread
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


threads = []
num_threads = os.cpu_count()
print(f'num_threads: {num_threads}')

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

if __name__ == '__main__':
    for t in threads:
        t.start()

    for t in threads:
        t.join()  # wait for all process to finish, while waiting block the main thread

    print('end main')
