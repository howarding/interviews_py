# v1.0 (9/6/2017)
import threading
from collections import deque

class stream:
    def __init__(self, deq):
        '''
        :param deque deq:
        '''
        self.deq = deq

    def hasNext(self):
        return True if self.deq else False

    def getNext(self):
        '''
        :rtype: tuple
        '''
        return self.deq.popleft()

    def push(self, tup):
        '''
        :param tuple tup:
        :return:
        '''
        self.deq.append(tup)



def getPairs(deques, val, ind, result):
    '''
    To produce all pairs for each new coming timestamp
    :param list deques:
    :param float val:
    :param int ind:
    :param list result:
    :return:
    '''
    other = 1 & ~ind
    while deques[other] and deques[other][0] < val - 1:
        deques[other].popleft()
    deques[ind].append(val)
    for ele in deques[other]:
        if ele > val + 1:
            break
        # print '(%.1f, %.1f)' % (val, ele)
        result.append((val, ele))



class queueThread(threading.Thread):
    '''
    To solve 2 problems:
    1. wait for blocking stream
    2. mutex lock to keep thread safe
    '''
    def __init__(self, stream, ind):
        '''
        :param stream stream:
        '''
        threading.Thread.__init__(self)
        self.stream = stream
        self.ind = ind

    def run(self):
        while True:     # spin lock (Busy waiting) for blocking streams
            try:
                (timestamp, val) = self.stream.getNext()
                mutex.acquire()         # mutex lock for critical region access
                getPairs(deques, timestamp, self.ind, result)
                mutex.release()
            except:
                continue



mutex = threading.Lock()


deq1 = deque(((0.2, 1), (1.4, 1), (3.0, 1)))
deq2 = deque(((1.0, 2), (1.1, 2), (3.5, 2)))

s1 = stream(deq1)
s2 = stream(deq2)

deques = [deque(), deque()]
result = []

t1 = queueThread(s1, 0)
t2 = queueThread(s2, 1)
t1.start()
t2.start()
t1.join()
t2.join()
print result


### From 1point3acres.com
### Not recommended

# q1, q2 = deque(), deque()
#
# while True:
#     val = stream1.read()
#     q1.push(val)
#     if q2:
#         if abs(val - q2[0]) < 1:
#             print(val, q2.popleft())
#         elif val > q2[0] + 1:
#             q2.popleft()
#     break