import threading, time
from multiprocessing import Condition


class SharedResource():
    def __init__(self):
        self.val = 0


# The class solving this problem
class RWLock:

    def __init__(self):
        self.cond = Condition()
        self.readers = 0

    def read_acquire(self):
        self.cond.acquire()
        self.readers += 1
        self.cond.release()

    def read_release(self):
        with self.cond:
            self.readers -= 1
            if (self.readers == 0):
                self.cond.notify_all()

    def write_acquire(self):
        self.cond.acquire()
        if (self.readers > 0):
            self.cond.wait()

    def write_release(self):
        self.cond.release()


def read(lock, res):
    while True:
        print ("start reading")
        lock.read_acquire()
        print("Reading1111:", lock.readers)
        time.sleep(0.8)

        res.val -= 1
        print("Reading2222:", res.val)
        lock.read_release()
        print("stop reading")


def write(lock, res):
    while True:
        lock.write_acquire()
        print("start writing")
        print("Writing")
        res.val += 1
        time.sleep(1)
        lock.write_release()
        print("stop writing")

if __name__ == '__main__':
    lock = RWLock()
    res = SharedResource()

    for i in range(2):

        t1 = threading.Thread(target=read, args=(lock, res,))

    t1.start()

    for i in range(1):

        t2 = threading.Thread(target=write, args=(lock, res,))

    t2.start()
