"""
Keys:
- A hard DP.
- There could at most have 1 "Absent" in a valid record. Therefore we could extract this case for later calculation.
- dp[i] represent valid cases number when we have i-1 days records. (With only "P" and "L").
- Overall, it is clearly a dp question, but a tough one to come up with the transfer relation.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [1, 2, 4, 7]

        # End with "P", "PL", "PLL"
        for i in range(4, n + 1):
            dp.append((dp[i-1] + dp[i-2] + dp[i-3]) % (10**9 + 7))

        result = dp[n]

        # Add absent cases.
        for j in range(n):
            result += dp[j] * dp[n-j-1]

        return result % (10**9 + 7)
