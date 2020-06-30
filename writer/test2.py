import queue
from filecmp import cmp
from operator import lt


class Job(object):
    def __init__(self, description):
        self.description = description
        # print('New job:', description)

    def __str__(self):
        return self.description


class Job2(object):
    def __init__(self, description):
        self.description = description
        # print('New job:', description)

    def __str__(self):
        res = []
        for i in range (8):
            res.append(i)

        return res


q = queue.PriorityQueue()

q.put((3, Job('pisze').__str__()))
q.put((5, Job2('czyta czyta').__str__()))
q.put((10, Job('pisze chujowo').__str__()))
q.put((1, Job('pisze wazne').__str__()))
q.put((2, Job2('czyta wazne').__str__()))


while q:
    print(q.get())
    # next_job = q.get()
    # print('Processing job:', next_job.description)
