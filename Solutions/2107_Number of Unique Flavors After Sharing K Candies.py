"""
Keys:
- Sliding Window.
"""


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        dct = collections.Counter(candies[k:])
        res = len(dct)
        for i in range(k, len(candies)):
            dct[candies[i]] -= 1
            if dct[candies[i]] == 0:
                del dct[candies[i]]
            dct[candies[i-k]] += 1
            res = max(res, len(dct))
        return res
