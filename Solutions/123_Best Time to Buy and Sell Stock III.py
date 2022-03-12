"""
Keys:
- "Buy and Sell Stock" are typical DP problems. It is a series of DP questions.

Complexity:
Time: O(n)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy = secondBuy = -prices[0]
        firstSell = secondSell = 0

        for price in prices:
            firstBuy = max(firstBuy, -price)
            firstSell = max(firstSell, firstBuy + price)
            secondBuy = max(secondBuy, firstSell - price)
            secondSell = max(secondSell, secondBuy + price)

        return secondSell
