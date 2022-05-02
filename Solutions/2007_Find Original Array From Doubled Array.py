"""
Keys:
- Basically, this is a problems which require Greedy thinking to solve.
- Idea is that the minimum number should always have its corresponding 2 times big number. Same idea applies for the maximum number.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2:
            return []
        counter = collections.Counter(changed)
        if counter[0] % 2:
            return []

        for num in sorted(counter):
            if counter[num] > counter[num * 2]:
                return []
            counter[num * 2] -= counter[num] if num != 0 else counter[num] // 2
            if counter[num * 2] == 0:
                del counter[num * 2]

        result = []
        for num, n in counter.items():
            for _ in range(n):
                result.append(num)

        return result
