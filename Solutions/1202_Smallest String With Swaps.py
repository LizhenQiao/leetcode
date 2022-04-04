"""
Complexity:
N is the number of empty cells.
Time: O(V*logV)
Space: O(V)

Time Complexity:
Construct Union-Find + E times Union + V times Find + worst case of sorting all connected partitions
O(V) + E * O(a(logV)) + V * (a(logV)) + V * logV
"""


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        l = len(s)
        parent = list(range(l))
        indexDict = collections.defaultdict(list)
        cDict = collections.defaultdict(list)
        result = ['a'] * l

        def find(x):
            if x == parent[x]:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for index1, index2 in pairs:
            union(index1, index2)

        for index in range(l):
            indexDict[find(index)].append(index)
            cDict[find(index)].append(s[index])

        for lst in cDict.values():
            lst.sort()

        for root in indexDict.keys():
            while indexDict[root]:
                result[indexDict[root].pop()] = cDict[root].pop()

        return "".join(result)
