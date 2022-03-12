"""
Keys:
- A slightly complicated version of "maximum sum subarray" / "minimum sum subarray" which are tipical questions of DP.

Complexity:
Time: O(n)
"""


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curmax = 0
        curmin = 0
        maxsum = -float('inf')
        minsum = float('inf')

        for num in nums:
            curmax = max(curmax, 0) + num
            curmin = min(curmin, 0) + num
            maxsum = max(maxsum, curmax)
            minsum = min(minsum, curmin)

        return max(maxsum, total - minsum) if maxsum > 0 else max(nums)
