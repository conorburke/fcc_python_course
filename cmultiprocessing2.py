from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time

def add_100(num: Value, lock: Lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            num.value += 1

def add_100A(arr: Array, lock: Lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for i in range(len(arr)):
                arr[i] += 1


def square(numbers, queue: Queue):
    for i in numbers:
        queue.put(i * i)


def make_negative(numbers, queue: Queue):
    for i in numbers:
        queue.put(-1 * i)


def cube(num):
    print(__name__)
    return num * num * num



# get this error if don't check for main module
# RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase
if __name__ == '__main__':
    
    numbers = range(10)
    pool = Pool()

    # map, apply, join, and close are important pool methods
    # this creates smart number of processes, and divies up work
    result = pool.map(cube, numbers)
    # execute one function
    # pool.apply(cube, numbers[:1])
    print(pool.__sizeof__())
    pool.close()
    pool.join()

    print(result)
    
    
    
    
    
    # q = Queue()
    # numbers = range(1, 6)

    # p1 = Process(target=square, args=(numbers, q))
    # p2 = Process(target=make_negative, args=(numbers, q))

    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # while not q.empty():
    #     print(q.get())




    # lock = Lock()
    # shared_array = Array('i', [0, 1, 2, 3, 4, 5])
    # print(f'Array at beginning is: {shared_array[:]}')

    # p1 = Process(target=add_100A, args=(shared_array, lock))
    # p2 = Process(target=add_100A, args=(shared_array, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print(f'Array at end is: {shared_array[:]}')




    # dtype, starting val
    # shared_number = Value('i', 0)
    # print(f'Number at beginning is: {shared_array[:]}')
    # p1 = Process(target=add_100, args=(shared_number, lock))
    # p2 = Process(target=add_100, args=(shared_number, lock))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print(f'Number at end is: {shared_number.value}')












# first mp video

# from multiprocessing import Process
# import os
# import time

# def square(n):
#     for i in range(n):
#         i * i
#         time.sleep(0.1)
#     print(__name__)
#     print('done one square')

# # get this error if don't check for main module
# # RuntimeError: An attempt has been made to start a new process before the current process has finished its bootstrapping phase
# if __name__ == '__main__':
#     processes = []
#     num_processes = os.cpu_count()
#     print(os.cpu_count())

#     # create proceses
#     for i in range(num_processes):
#         p = Process(target=square, args=(100,))
#         processes.append(p)

#     for p in processes:
#         p.start()

#     # waitin for processes to finish; block main thread until they all do
#     for p in processes:
#         p.join()

#     print('end main')