"""
Keys:
- Ask for k minimum / maximum. => A tipical problem which could be solved by using Heap.
- The solution is actually very delicate for me, uses the order of the matrix.

Complexity:
x refers to min(k, m)
time: O(x*logx)
space: O(x)
"""


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        heap = []
        for i in range(min(m, k)):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        while k > 1:
            _, row, column = heapq.heappop(heap)
            if column < m-1:
                heapq.heappush(heap, (matrix[row][column+1], row, column+1))
            k -= 1

        return heap[0][0]
