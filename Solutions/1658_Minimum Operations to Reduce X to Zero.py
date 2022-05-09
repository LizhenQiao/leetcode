"""
Keys:
- The intuition of the solution is not obvious.
- We convert original question "Minimum Operations to Reduce X to Zero" to "Get maximum length of subarray that sum up to `sum(nums) - x`"

Complexity:
Time: O(n)
Space: O(n) 
"""


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        summ = sum(nums)
        # Corner case when all number should be removed from nums array.
        if summ == x:
            return len(nums)
        target = summ - x
        maxl = 0
        dct = {}
        dct[0] = -1
        tmpsum = 0

        for index, num in enumerate(nums):
            tmpsum += num
            if (tmpsum - target) in dct:
                maxl = max(maxl, index - dct[tmpsum-target])
            if tmpsum in dct:
                continue
            dct[tmpsum] = index

        return (len(nums) - maxl) if maxl > 0 else -1
