"""
Keys:
- Utilize stack to simulate.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = []
        tmpl = 0
        maxl = 0

        for s in input.split("\n"):
            tabNum = s.count("\t")
            while stack and stack[-1][1] >= tabNum:
                popName, _ = stack.pop()
                tmpl -= len(popName) + 1
            fileName = s[tabNum:]
            tmpl += len(fileName) + 1
            stack.append((fileName, tabNum))
            if "." in fileName:
                maxl = max(maxl, tmpl-1)

        return maxl
