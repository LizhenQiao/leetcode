"""
Keys:
- A typical heap question.
"""


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        l = len(heights)

        for i in range(1, l):
            cost = heights[i] - heights[i-1]
            if cost <= 0:
                continue
            if len(heap) < ladders:
                heapq.heappush(heap, cost)
                continue
            heapq.heappush(heap, cost)
            popcost = heapq.heappop(heap)
            bricks -= popcost
            if bricks < 0:
                return i - 1

        return l - 1
