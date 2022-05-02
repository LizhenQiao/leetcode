"""
Keys:
- Obviously a DP problem.
- A more complicated version of leetcode 1014.


Complexity:
time: O(m*n)
space: O(n)
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0][:]

        for i in range(1, m):
            lst = dp[:]
            leftBest = rightBest = -float('inf')

            for j in range(n):
                leftBest = max(leftBest, lst[j] + j)
                dp[j] = points[i][j] - j + leftBest

            for j in range(n-1, -1, -1):
                rightBest = max(rightBest, lst[j] - j)
                dp[j] = max(dp[j], points[i][j] + j + rightBest)

        return max(dp)
