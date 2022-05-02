"""
Keys:
- A variant of Leetcode227. Generally similar idea.
- Code might be compressed a little bit. But logic of this solution is optimimal.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        tmpnum = 0
        sign = "+"

        for c in (s + "+"):
            if c.isdigit():
                tmpnum = tmpnum * 10 + int(c)
            else:
                if c == "(":
                    stack.append(sign)
                    stack.append("(")
                    sign = "+"
                elif c == ")":
                    if sign == "+":
                        stack.append(tmpnum)
                    else:
                        stack.append(-tmpnum)
                    tmpnum = 0
                    while stack and stack[-1] != "(":
                        tmpnum += stack.pop()
                    stack.pop()
                    tmpsign = stack.pop()
                    if tmpsign == "+":
                        stack.append(tmpnum)
                    elif tmpsign == "-":
                        stack.append(-tmpnum)
                    tmpnum = 0
                elif c in "+-":
                    if sign == "+":
                        stack.append(tmpnum)
                    else:
                        stack.append(-tmpnum)
                    sign = c
                    tmpnum = 0

        return sum(stack)
