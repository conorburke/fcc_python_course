from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(queue: Queue, lock: Lock):
    # could use poison pill technique and not rely on daemon thread and queue being done
    # basically this will run until que says its done with everything
    while True:
        value = queue.get()
        
        # simulate processing
        with lock:
            print(f'in current thread: {current_thread().name} got value: {value}')

        queue.task_done()


if __name__ == '__main__':

    q = Queue()
    lock = Lock()

    num_threads = 5

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,lock))
        # use daemon thread so it dies when main thread dies
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)
    
    # won't execute until all unfinished tasks is zero, so when task_done is called however many times put() was
    q.join()









    # q = Queue()

    # q.put(1)
    # q.put(2)
    # q.put(3)

    # first = q.get()
    # print(first)

    # check empty
    # q.empty()

    # use q.task_done() when done with processing task
    # q.join() blocks the main thread and wait until all elements in q are processed







# # simulate database for exercise
# database_value = 0

# def increase(lock: Lock):
    
#     global database_value
#     # lock.acquire()
#     # local_copy = database_value

#     # # simulate processing
#     # local_copy += 1
#     # time.sleep(0.1)

#     # database_value = local_copy
#     # lock.release()

#     # same as above but always releases
#     with lock:
#         local_copy = database_value

#         # simulate processing
#         local_copy += 1
#         time.sleep(0.1)

#         database_value = local_copy

# if __name__ == '__main__':

#     print(f'start vale: {database_value}')

#     lock = Lock()

#     thread1 = Thread(target=increase, args=(lock,))
#     thread2 = Thread(target=increase, args=(lock,))

#     thread1.start()
#     thread2.start()

#     thread1.join()
#     thread2.join()

#     print(f'end value: {database_value}')

#     print('end main')












# threads can be used similar to last multiprocessing

# from threading import Thread
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
#     threads = []
#     num_threads = os.cpu_count() * 2
#     print(os.cpu_count())

#     # create proceses
#     for i in range(num_threads):
#         t = Thread(target=square, args=(100,))
#         threads.append(t)

#     for t in threads:
#         t.start()

#     # waitin for threads to finish; block main thread until they all do
#     for t in threads:
#         t.join()

#     print('end main')