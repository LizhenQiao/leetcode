"""
Keys:
- Buy and Sell problem => typical DP.
- Status: Holding; Not Holding;

Complexity:
Time: O(n)
"""


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        dp = [[0] * 2 for _ in range(l)]
        dp[0][0] = -prices[0]
        for i in range(1, l):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)

        return max(dp[-1][1], 0)
