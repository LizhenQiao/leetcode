"""
Keys:
- Almost same question to Leetcode 907. Refer to solution of that problem.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        summ = 0

        stack = []
        lst1 = [float('inf')] + nums[:] + [float('inf')]
        for index, num in enumerate(lst1):
            while stack and lst1[stack[-1]] < num:
                popIndex = stack.pop()
                summ += lst1[popIndex] * \
                    (popIndex - stack[-1]) * (index - popIndex)
            stack.append(index)

        stack = []
        lst2 = [-float('inf')] + nums[:] + [-float('inf')]
        for index, num in enumerate(lst2):
            while stack and lst2[stack[-1]] > num:
                popIndex = stack.pop()
                summ -= lst2[popIndex] * \
                    (popIndex - stack[-1]) * (index - popIndex)
            stack.append(index)

        return summ
