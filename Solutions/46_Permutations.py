"""
Keys:
- Optimize: we could manipulate `nums`, instead of have a `lst`. This is the part I find a little triky and not that intuitive to me.

Complexity:
Time: O(n * n!)

Cause we use backtracking, thus we need O(n!) to find all the possible solutions. Plus we will need O(n) to copy each permutation to the result list.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        result = []
        lst = []

        def helper(index):
            if index == l:
                result.append(lst[:])
                return None
            for num in nums:
                if num not in lst:
                    lst.append(num)
                    helper(index + 1)
                    lst.pop()

        helper(0)
        return result


# Optimize: we could manipulate `nums`, instead of have a `lst`. This is the part I find a little triky.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        l = len(nums)

        def helper(index):
            if index == l-1:
                result.append(nums[:])
                return None
            for i in range(index, l):
                nums[i], nums[index] = nums[index], nums[i]
                helper(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        helper(0)
        return result
