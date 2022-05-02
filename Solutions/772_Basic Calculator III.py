"""
Keys:
- A variant of Leetcode227, Leetcode224. Basically the same, nothing new.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        tmpnum = 0

        for c in (s + "+"):
            if c.isdigit():
                tmpnum = tmpnum * 10 + int(c)
            else:
                if c == "(":
                    stack.append(sign)
                    stack.append("(")
                    sign = "+"
                else:
                    if sign == "+":
                        stack.append(tmpnum)
                    elif sign == "-":
                        stack.append(-tmpnum)
                    elif sign == "*":
                        stack.append(stack.pop() * tmpnum)
                    elif sign == "/":
                        stack.append(int(stack.pop() / tmpnum))
                    tmpnum = 0
                    if c != ")":
                        sign = c
                    else:
                        while stack[-1] != "(":
                            tmpnum += stack.pop()
                        stack.pop()
                        sign = stack.pop()
        return sum(stack)
