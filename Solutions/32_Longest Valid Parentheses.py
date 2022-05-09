"""
Keys:
- The idea for this question is to keep stack[-1] to be `the last unvalid ")"'s index`. Then the question become much easier. 

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        stack.append(-1)
        maxl = 0

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                maxl = max(maxl, i - stack[-1])

        return maxl
