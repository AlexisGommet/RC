from threading import Thread, Lock
from time import sleep


counter = 0

def increase(by):
    global counter

    sleep(0.1)
    
    lock.acquire()
    counter += by
    lock.release()
    
    print(f'counter={counter}')
    
lock = Lock()

# create threads
t1 = Thread(target=increase, args=(10,))
t2 = Thread(target=increase, args=(20,))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

print(f'The final counter is {counter}')