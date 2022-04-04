"""
Keys:
- Distance in a positive weighted graph -> Dijkstra's Algorithm.
- Based the idea of Dijkstra's Algorithm. The code was written as below.

Complexity:
Time: O(V + E*logV)
Space: O(V)

"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        connections = collections.defaultdict(list)
        distances = [0] + [float('inf')] * n
        nodeHeap = []
        visited = set()

        distances[k] = 0
        heapq.heappush(nodeHeap, (0, k))
        for node1, node2, d in times:
            connections[node1].append((node2, d))

        while nodeHeap:
            distance, node = heapq.heappop(nodeHeap)
            if node in visited:
                continue
            for node0, d in connections[node]:
                if node0 in visited:
                    continue
                if distance + d < distances[node0]:
                    distances[node0] = distance + d
                    heapq.heappush(nodeHeap, (distance + d, node0))
            visited.add(node)

        return max(distances) if len(visited) == n else -1
