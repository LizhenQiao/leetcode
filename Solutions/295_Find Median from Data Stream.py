"""
Keys:
- Two heap to implement median finder. (Which is a very classic data structure implementation.)

Complexity:
time: O(logn)
space: O(n)
"""


class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        if len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        elif len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self) -> float:
        return -self.maxheap[0] if len(self.maxheap) > len(self.minheap) else (-self.maxheap[0] + self.minheap[0]) / 2
