"""
Keys:
- Basically just a normal BFS.

Complexity:
Time: O(n)
Space: O(n)

"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        n = len(grid)
        if n == 1:
            return 1
        visited = {}
        queue = collections.deque()
        queue.append(tuple((0, 0)))
        visited[tuple((0, 0))] = 1

        while queue:
            node = queue.popleft()
            distance = visited[node]
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if not 0 <= node[0] + i < n or not 0 <= node[1] + j < n or grid[node[0] + i][node[1] + j] != 0:
                        continue
                    newNode = tuple((node[0] + i, node[1] + j))
                    newDistance = distance + 1
                    if newNode not in visited:
                        visited[newNode] = newDistance
                        queue.append(newNode)
                    if newNode[0] == n-1 and newNode[1] == n-1:
                        return newDistance
        return -1
