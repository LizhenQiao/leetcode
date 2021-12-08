"""
Keys:
- DP
- Start from i*i (line23)

Complexity:
Time: O(n*loglogn)
Space: O(n)
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        primeCounter = 0
        if n < 2:
            return 0
        lst = [True] * n

        for i in range(2, n):
            if lst[i]:
                primeCounter += 1
                # Start from i*i
                for j in range(i*i, n, i):
                    lst[j] = False

        return primeCounter
