"""
Keys:
- Subarray question => typical DP.

Complexity:
Time: O(mn)
"""


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[0] * (l1 + 1) for _ in range(l2 + 1)]
        result = 0

        for i in range(l1):
            for j in range(l2):
                if nums1[i] == nums2[j]:
                    dp[j+1][i+1] = dp[j][i] + 1
                    result = max(result, dp[j+1][i+1])

        return result
