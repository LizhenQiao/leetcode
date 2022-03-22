"""
Keys:
- Ask for k minimum / maximum. => A tipical problem which could be solved by using Heap.
- Could using either min-heap or max-heap. Max-heap would save space for k-minimum problems. Vice versa.

Complexity:
time: O(m*n) - could be O(m*logn) if using binary search for counting 1 of each row.
space: O(k)
"""


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        result = []
        heap = []

        for i in range(m):
            counter = 0
            for person in mat[i]:
                if person == 1:
                    counter += 1
                if person == 0 or counter == len(mat[0]):
                    if len(heap) < k:
                        heapq.heappush(heap, (-counter, -i))
                    else:
                        if counter < -heap[0][0]:
                            heapq.heappop(heap)
                            heapq.heappush(heap, (-counter, -i))
                    break
        while heap:
            result.append(-heapq.heappop(heap)[1])
        return result[::-1]
