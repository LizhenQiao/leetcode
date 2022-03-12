"""
Keys:
- Ask for number of ways => could be DP.
- Directly define a Status Transition Rule => Intuitive to think in the way of DP. 

Complexity:
Time: O(n)
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """
        End by a/e/i/o/u
        0: 'a'
        1: 'e'
        2: 'i'
        3: 'o'
        4: 'u'
        """
        dp = [[1] * 5 for _ in range(n)]

        for i in range(1, n):
            dp[i][0] = dp[i-1][1] + dp[i-1][4] + dp[i-1][2]
            dp[i][1] = dp[i-1][2] + dp[i-1][0]
            dp[i][2] = dp[i-1][1] + dp[i-1][3]
            dp[i][3] = dp[i-1][2]
            dp[i][4] = dp[i-1][2] + dp[i-1][3]

        return sum(dp[-1]) % (10 ** 9 + 7)
