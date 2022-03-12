"""
Keys:
- DP. (Typical Status Transition of String problems.)
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        if l1 == 0:
            return s2 == s3
        if l2 == 0:
            return s1 == s3
        dp = [[False] * (l1 + 1) for _ in range(l2 + 1)]
        dp[0][0] = True

        for i in range(1, l1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[0][i] = True
            else:
                break
        for j in range(1, l2 + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[j][0] = True
            else:
                break

        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if s1[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j-1]
                if s2[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i-1][j]
        return dp[-1][-1]
