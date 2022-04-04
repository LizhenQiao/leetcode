"""
Keys:
- Baisc idea of Bellman Ford Algorithm.
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        lst = [float('inf')] * n
        connections = collections.defaultdict(list)

        lst[src] = 0
        for s, d, distance in flights:
            connections[d].append((s, distance))

        for _ in range(k + 1):
            newLst = lst[:]
            for i in range(n):
                if i == src:
                    continue
                for j, distance in connections[i]:
                    newLst[i] = min(newLst[i], lst[j] + distance)
            lst = newLst[:]

        return lst[dst] if lst[dst] != float('inf') else -1
