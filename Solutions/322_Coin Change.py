"""
Keys:
- "Coin Change" is a typical DP problem, and the status transition is typical.  
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i-coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
