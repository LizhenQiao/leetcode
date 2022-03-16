"""
Keys:
- O(n) time, O(1) space solution
- Note that num in nums are from [1, n], utilize the range of nums and index of nums.

Complexity:
Time: O(n)
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            nums[abs(num)-1] = abs(nums[abs(num)-1]) * -1

        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
