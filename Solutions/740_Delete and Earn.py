"""
Keys:
- Ask for maximum && Former choices influence latter choices => DP

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dct = collections.Counter(nums)
        pick = unpick = 0
        prevNum = -float('inf')
        for num in sorted(dct):
            if num - 1 == prevNum:
                pick, unpick = unpick + num * dct[num], max(pick, unpick)
            else:
                pick, unpick = max(pick, unpick) + num * \
                    dct[num], max(pick, unpick)
            prevNum = num
        return max(pick, unpick)
