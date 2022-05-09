"""
Keys:
- Prefix Sum.

Complexity:
Time: O(n)
Space: O(n) 
"""


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dct = collections.defaultdict(int)
        dct[0] = 1
        summ = 0
        result = 0

        for num in nums:
            summ += num
            x = summ % k
            result += dct[x]
            dct[x] += 1
        return result
