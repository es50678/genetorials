from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(1)


processes = []
num_processes = os.cpu_count()

for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

if __name__ == '__main__':
    for p in processes:
        p.start()

    for p in processes:
        p.join()  # wait for all process to finish, while waiting block the main thread

    print('end main')
