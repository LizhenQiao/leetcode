"""
Keys:
- Two pointer, Sliding Window (Pretty intuitive)

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        maxl = 0
        haveFlipped = False
        for r in range(len(nums)):
            if not nums[r]:
                if not haveFlipped:
                    haveFlipped = True
                else:
                    while nums[l]:
                        l += 1
                    l += 1
            maxl = max(maxl, r - l + 1)

        return maxl
