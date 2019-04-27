# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.
#
# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
#
# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].
#
# Note:
# You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
import heapq


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        result = list()
        counter = dict()
        max_heap = list()
        min_heap = list()

        i = 0
        while i < k:
            heapq.heappush(max_heap, (-nums[i], nums[i]))
            i += 1
        for count in range(k / 2):
            heapq.heappush(min_heap, heapq.heappop(max_heap)[1])

        while True:
            if k % 2:
                result.append(max_heap[0][1])
            else:
                result.append(max_heap[0][1] / 2.0 + min_heap[0] / 2.0)

            if i == len(nums):
                break
            m = nums[i-k]
            n = nums[i]
            balance = 0
            i += 1

            if m <= max_heap[0][1]:
                balance -= 1
                if m == max_heap[0][1]:
                    heapq.heappop(max_heap)
                else:
                    if m not in counter:
                        counter[m] = 0
                    counter[m] += 1
            else:
                balance += 1
                if m == min_heap[0]:
                    heapq.heappop(min_heap)
                else:
                    if m not in counter:
                        counter[m] = 0
                    counter[m] += 1

