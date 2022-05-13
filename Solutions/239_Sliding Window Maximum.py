"""
Keys:
- (Heap / Monotonic Queue) [Practice more after practicing monotonic stack]
- Sliding window minimum/maximum = monotonic queue.
- Actually for monotonic queue, the idea is pretty much the same with monotonic stack, except that because of the sliding window's
restriction, we need to make stack a queue in order to efficiently delete elements which are out of boundary.
"""

# Heap


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        heap = [(-num, index) for index, num in enumerate(nums[:k])]
        heapq.heapify(heap)
        result.append(-heap[0][0])

        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] < i-k+1:
                heapq.heappop(heap)
            result.append(-heap[0][0])

        return result


# Monotonic Queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        queue = collections.deque()

        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        result.append(nums[queue[0]])

        for i in range(k, len(nums)):
            if queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])

        return result
