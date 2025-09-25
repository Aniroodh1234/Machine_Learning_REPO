### Multithreading
# to perform a single task more spedly and efficiently we craete multiple threads

# Multithreading is a technique where multiple threads are spawned by a process to perform tasks concurrently.
# A thread is a lightweight process, and multiple threads within the same process share the same data space.
# This allows them to communicate with each other more easily than if they were separate processes.
# Threads are used to perform tasks that are I/O-bound or require waiting for external resources.
# In Python, the threading module is used to create and manage threads.
# The threading module provides a way to create and manage threads in Python.
# It allows you to create threads, start them, and wait for them to finish.
# The threading module also provides a way to synchronize threads and manage shared resources.


## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.



# in this code we are using single thread 

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"number: {i}")

def print_letters():
    for letter in 'abcde':
        time.sleep(2)
        print(f"letters: {letter}")

t = time.time()
# print_numbers()
# print_letters()

finished_time = time.time() - t
print(finished_time)



# here multiple threading is used so both functions are runned concurrently
import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
def print_letter():
    for i in 'abcde':
        time.sleep(2)
        print(f"Letter: {i}")

# creating threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letter)

t = time.time()

#start thread
t1.start()
t2.start()

# wait for thread to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)

