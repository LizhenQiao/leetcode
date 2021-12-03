"""
Keys:

Bitwise operation
state transformation with two state

Complexity:
Time: O(n)
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        state1 = state2 = 0
        for num in nums:
            state1 = ~state2 & (state1 ^ num)
            state2 = ~state1 & (state2 ^ num)
        return state1
