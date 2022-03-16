"""
Complexity:
Time: O(2^n)

Same as DFS
"""


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dct = collections.defaultdict(int)
        dct[0] = 1
        for num in nums:
            dct_new = collections.defaultdict(int)
            for summ, freq in dct.items():
                dct_new[summ + num] += freq
                dct_new[summ - num] += freq
            dct = dct_new
        return dct[target]
