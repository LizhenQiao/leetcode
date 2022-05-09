"""
Keys:
- It is a fundamental question to solve for many parentheses questions.

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for c in s:
            if c == "(":
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    right += 1
        return left + right
