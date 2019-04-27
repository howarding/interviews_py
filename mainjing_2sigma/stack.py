# Implement a stack with methods:
#     pop,
#     push,
#     minValue,
#     maxValue,
#     average,
#     most frequent number,
#     medium

import heapq

class Stack(object):
    def __init__(self):
        self.nums = list()
        self.maxs = list()
        self.mins = list()
        self.avg = 0.0
        self.num_count = dict()
        self.count_nums = dict()
        self.maxCount = 0
        self.count_nums[0] = set()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        total = len(self.nums)
        self.avg = self.avg * total / (total + 1) + x * 1.0 / (total + 1)

        self.nums.append(x)
        self.maxs.append(max(self.maxs[-1], x))
        self.mins.append(min(self.mins[-1], x))

        if x not in self.num_count:
            self.num_count[x] = 0
        self.num_count[x] += 1
        count = self.num_count[x]
        if count not in self.count_nums:
            self.count_nums[count] = set()
        self.count_nums[count].insert(x)
        if count > 1:
            self.count_nums[count-1].erase(x)
        self.maxCount = max(self.maxCount, count)




    def pop(self):
        """
        :rtype: void
        """
        total = len(self.nums)
        self.avg = (self.avg * total - self.nums[-1]) / (total - 1) if total > 1 else 0

        x = self.nums[-1]
        self.nums.pop()
        self.maxs.pop()
        self.mins.pop()

        count = self.num_count[x]
        self.num_count[x] -= 1
        self.count_nums[count].erase(x)
        if not self.count_nums[count]:
            self.maxCount -= 1
        if count > 1:
            self.count_nums[count-1].insert(x)





    def minValue(self):
        return self.mins[-1]

    def maxValue(self):
        return self.maxs[-1]

    def average(self):
        return self.avg

    def mostFreqNum(self):
        return self.count_nums[self.maxCount]

