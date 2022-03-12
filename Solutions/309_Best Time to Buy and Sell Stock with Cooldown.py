"""
Keys:
- "Buy and Sell Stock" are typical DP problems. It is a series of DP questions.
- For this question we extract 3 status.
holding; not holding + just sell; not holding + not just sell;
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        dp = [[0] * 3 for _ in range(l)]
        dp[0][0] = -prices[0]

        for i in range(1, l):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])

        return max(dp[-1])
