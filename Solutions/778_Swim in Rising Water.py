"""
Keys:
- BFS with Heap. The idea is similar to Dijkstra's Algorithm.
- Note that heap operation is O(logn).

Complexity:
Time: O(mn * log(mn))
"""


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mintimes = {}
        heap = []
        heapq.heappush(heap, (grid[0][0], (0, 0)))

        while heap:
            time, (y, x) = heapq.heappop(heap)
            if (y, x) in mintimes:
                continue
            else:
                mintimes[(y, x)] = time
            if (y, x) == (m-1, n-1):
                return time
            for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newy, newx = y + dy, x + dx
                if not 0 <= newy < m or not 0 <= newx < n or (newy, newx) in mintimes:
                    continue
                heapq.heappush(
                    heap, (max(time, grid[newy][newx]), (newy, newx)))
