"""
Keys:
- Obviously a recursion with backtracking problem.

Complexity:
Time: O(2^n)
Space: O(2^n)
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        lst = []

        def helper(l, r):
            if l == r == n:
                result.append("".join(lst[:]))
                return None
            if l < n:
                lst.append("(")
                helper(l+1, r)
                lst.pop()
            if r < l:
                lst.append(")")
                helper(l, r+1)
                lst.pop()

        helper(0, 0)
        return result
