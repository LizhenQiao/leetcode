"""
Keys:
- DP
- loop coins first to easier get rid of duplicates.

Complexity:
Time: O(k*n)
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[-1]
