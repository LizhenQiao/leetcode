"""
Keys:
- A commonly used way of compressing DP into one pass. I've seen several problems related to this skill. (1937, Buy and Sell Stock III)


Complexity:
time: O(n)
space: O(1)
"""


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        best1 = best2 = -float('inf')

        for index, value in enumerate(values):
            best2 = max(best2, best1 + value - index)
            best1 = max(best1, value + index)

        return best2
