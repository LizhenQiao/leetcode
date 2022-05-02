"""
Keys:
- DP problem. The dynamic relationship is not that obvious to me.
- Use hash table to store state instead of array. (Should be more familiar with it.)
- Use recursion to accomplish DP instead of iteration. (Not familiar, though it should be intuitive for this question, 
  cause the dynamic relationship is not simple from left to right or something like this.)

Complexity:
Time: O(n^3)
Space: O(n^2)
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        dct = {}

        def helper(i, j):
            if i == j:
                return 1
            if (i, j) in dct:
                return dct[(i, j)]
            if s[i] == s[j]:
                dct[(i, j)] = helper(i, j - 1)
                return dct[(i, j)]
            minTurn = float('inf')
            for k in range(i, j):
                minTurn = min(minTurn, helper(i, k) + helper(k+1, j))
            dct[(i, j)] = minTurn
            return dct[(i, j)]

        return helper(0, len(s) - 1)
