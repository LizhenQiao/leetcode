"""
Keys:
- "Buy and Sell Stock" are typical DP problems. It is a series of DP questions.

Complexity:
Time: O(k*n)
"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        buys = [-prices[0]] * (k + 1)
        sells = [0] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                buys[i] = max(buys[i], sells[i-1] - price)
                sells[i] = max(sells[i], buys[i] + price)

        return sells[-1]
