"""
Keys:
- Sliding window.
"""


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        tmpsum = 0
        left = 0
        numSet = set()
        maxsum = -float('inf')

        for right in range(len(nums)):
            while nums[right] in numSet:
                numSet.remove(nums[left])
                tmpsum -= nums[left]
                left += 1
            numSet.add(nums[right])
            tmpsum += nums[right]
            maxsum = max(maxsum, tmpsum)

        return maxsum
