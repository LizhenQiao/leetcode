"""
Keys:
- Clearly a MST question. Practice Kruskal's Algorithm and Prim's Algorithm.

Complexity:
Refer to the .md part. No difference.
"""

# Kruskal's Algorithm.


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        parent = {}
        for point in points:
            parent[tuple(point)] = tuple(point)
        l = 0
        num = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        connections = []
        for i in range(n):
            point1 = points[i]
            for j in range(i+1, n):
                point2 = points[j]
                distance = abs(point1[0] - point2[0]) + \
                    abs(point1[1] - point2[1])
                connections.append((tuple(point1), tuple(point2), distance))
        connections.sort(key=lambda x: x[2])

        for point1, point2, d in connections:
            root1 = find(point1)
            root2 = find(point2)
            if root1 == root2:
                continue
            union(tuple(point1), tuple(point2))
            l += d
            num += 1
            if num == n-1:
                return l


# Prim's Algorithm.
# This code is just a copy of others. The names of variables are not clear to me, but the idea is the same.
class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        def manhattan(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])

        ans, n = 0, len(p)
        seen = set()
        vertices = [(0, (0, 0))]

        while len(seen) < n:
            w, (u, v) = heapq.heappop(vertices)
            if v in seen:
                continue
            ans += w
            seen.add(v)
            for j in range(n):
                if j not in seen:
                    heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))
        return ans
