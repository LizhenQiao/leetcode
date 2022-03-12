"""
Keys:
- Ask for number of ways + have clear status transition => DP.
- However, the Status and Transition are not so intuitive for me at the first time.

Complexity:
Time: O(n)
"""


class Solution:
    def numTilings(self, n: int) -> int:
        # handle base case scenarios
        if n <= 2:
            return n
        # f[k]: number of ways to "fully cover a board" of width k
        f = [0] * n
        # p[k]: number of ways to "partially cover a board" of width k
        p = [0] * n
        # initialize f and p with results for the base case scenarios
        f[0] = 1
        f[1] = 2
        p[1] = 2

        for k in range(2, n):
            f[k] = (f[k - 1] + f[k - 2] + p[k - 1])
            p[k] = (p[k - 1] + 2 * f[k - 2])

        return f[-1] % (10 ** 9 + 7)
