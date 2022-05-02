"""
Keys:
- BFS.
- We could slightly simplify this question by performing BFS from Houses to Empty Land instead of from Empty Land to Houses(
  which is probably more intuitive). Basically, when there are fewer houses than empty lands, then this approach will require
  less time than the previous approach and vice versa.

Complexity:
Time: O(m^2 * n^2)
Space: O(m*n)
"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distances = [[0] * n for _ in range(m)]
        result = float('inf')

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    distances[i][j] = float('inf')
                    visited = set()
                    queue = collections.deque()
                    queue.append(((i, j), 0))
                    while queue:
                        (y, x), d = queue.popleft()
                        if (y, x) in visited or not 0 <= y < m or not 0 <= x < n:
                            continue
                        if not (y == i and x == j) and grid[y][x] != 0:
                            continue
                        distances[y][x] += d
                        visited.add((y, x))
                        queue.append(((y+1, x), d+1))
                        queue.append(((y-1, x), d+1))
                        queue.append(((y, x+1), d+1))
                        queue.append(((y, x-1), d+1))
                    for i0 in range(m):
                        for j0 in range(n):
                            if (i0, j0) not in visited:
                                distances[i0][j0] = float('inf')

        for i in range(m):
            for j in range(n):
                result = min(result, distances[i][j])

        return result if result != float('inf') else -1
