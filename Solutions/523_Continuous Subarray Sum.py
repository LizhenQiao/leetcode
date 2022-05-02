"""
Keys:
- The solution is interesting and clever. Use `mod calculation`, `prefix sum` and `hash table` to make this check O(n). 

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dct = {0: -1}
        summ = 0

        for index, num in enumerate(nums):
            summ += num
            x = summ % k
            if x not in dct:
                dct[x] = index
            else:
                if index - dct[x] > 1:
                    return True

        return False
