"""
Keys:
- Stack.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        tmpstr = ""

        for c in s:
            if c == "(":
                stack.append(tmpstr)
                tmpstr = ""
            elif c == ")":
                if stack:
                    tmpstr = stack.pop() + "(" + tmpstr + ")"
            elif c.islower():
                tmpstr += c
            else:
                return False

        while stack:
            tmpstr = stack.pop() + tmpstr

        return tmpstr
