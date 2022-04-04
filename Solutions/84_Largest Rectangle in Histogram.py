"""
Keys:
- largest area: Obviously a typical problem which could be solved by maximum stack / minimum stack.
- While analyzing the calculation process, it is clearly that if we add zero at the beginning and at the end of the heights list. We could get rid of the corner case discussion.
- Get more familiar with similar questions like this would make this more intuitive.

Complexity:
Time: O(n)
Space: O(n)

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        l = len(heights)
        maxs = 0
        heights = [0] + heights + [0]
        stack = []

        for i in range(l+2):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                maxs = max(maxs, (i - stack[-1] - 1) * heights[index])
            stack.append(i)

        return maxs
