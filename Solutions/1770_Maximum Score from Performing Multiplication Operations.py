"""
Keys:
- Find out it is a DP.
- Come up with the status transition.

Complexity:
Time: O(m^2)
Space: O(m^2)
"""


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        result = -float('inf')
        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + multipliers[i-1] * nums[i-1]
            dp[0][i] = dp[0][i-1] + multipliers[i-1] * nums[-i]

        for i in range(1, m + 1):
            for j in range(1, m - i + 1):
                dp[i][j] = max(dp[i-1][j] + multipliers[i+j-1] *
                               nums[i-1], dp[i][j-1] + multipliers[i+j-1] * nums[-j])

        for i in range(m + 1):
            result = max(result, dp[i][m-i])

        return result
