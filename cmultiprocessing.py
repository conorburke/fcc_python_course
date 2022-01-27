# first mp video

from multiprocessing import Process
import os
import time

def square(n):
    for i in range(n):
        i * i
        time.sleep(0.1)
    print(__name__)
    print('done one square')

# get this error if don't check for main module
# RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase
if __name__ == '__main__':
    processes = []
    num_processes = os.cpu_count()
    print(os.cpu_count())

    # create proceses
    for i in range(num_processes):
        p = Process(target=square, args=(10,))
        processes.append(p)

    for p in processes:
        p.start()

    # waitin for processes to finish; block main thread until they all do
    for p in processes:
        p.join()

    print('end main')