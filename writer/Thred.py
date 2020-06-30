import queue
import threading
import time
from random import random

list = []
isWriterActive = False
isReaderActive = False


class Writer(threading.Thread):

    def __init__(self, begin, txt, time, count, name):
        threading.Thread.__init__(self)
        self.name = name
        self.begin = begin
        self.txt = txt
        self.time = time
        self.count = count

    def run(self):

        global isWriterActive

        for i in range(self.count):
            if self.begin == 1:
                time.sleep(1)
                self.begin = 0

            if not isReaderActive:
                lock.acquire()
                isWriterActive = True
                time.sleep(self.time)
                list.append(self.txt)
                print(self.name, 'pisze', list)
                isWriterActive = False
                lock.release()


def set_interval(func, sec):
    global isWriterActive

    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)

    t.start()
    if not isWriterActive:
        isWriterActive = True
        return isWriterActive
    else:
        isWriterActive = False
        return isWriterActive


def write():
    global isWriterActive

    if not isWriterActive:
        roll = random.randint(1, 3)
        print("You rolled: " + str(roll))
        if roll == 3:
            isWriterActive = True


class Reader(threading.Thread):

    def __init__(self, begin, time, count, name):
        threading.Thread.__init__(self)
        self.name = name
        self.begin = begin
        self.time = time
        self.count = count

    def run(self):
        global isReaderActive

        global isWriterActive

        set_interval(write, 1)

        if self.begin != 0:
            time.sleep(self.begin)
            self.begin = 0

        # if not isWriterActive:
        isReaderActive = True
        print(self.name, 'czyta', list)
        time.sleep(self.time)
        isReaderActive = False


q = queue.PriorityQueue()
lock = threading.Lock()

write1 = Writer(1, 'ala', 2, 2, 'pisarz 1')
write2 = Writer(1, 'ma', 2, 2, 'pisarz 2')
read1 = Reader(0, 1, 1, 'czytelnik 1')
read2 = Reader(3, 1, 2, 'czytelnik 2')
read3 = Reader(0, 1, 1, 'czytelnik 3')

q.put((1, read1.start()))
# q.put((1, read2.start()))
# q.put((1, read3.start()))
q.put((2, write1.start()))
# q.put((2, write2.start()))
