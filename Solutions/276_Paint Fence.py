"""
Keys:
- Number of Ways question => Could be DP.
- Status transition.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k ** 2

        dp = [0] * n
        dp[0] = k
        dp[1] = k ** 2

        for i in range(2, n):
            dp[i] = (k - 1) * (dp[i-1] + dp[i-2])

        return dp[-1]
