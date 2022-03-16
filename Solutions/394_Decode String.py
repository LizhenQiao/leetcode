"""
Keys:
- The string transformation (usually have some signs such as parentheses.) is a 
typical series of questions using stack. The details of the questions might be a 
little different from each other. The idea of them are quite similar and intuitive.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curstr = ""
        curnum = 0

        for c in s:
            if c == "[":
                stack.append((curnum, curstr))
                curstr = ""
                curnum = 0
            elif c == "]":
                popnum, popstr = stack.pop()
                curstr = popstr + popnum * curstr
            elif c.isdigit():
                curnum = curnum * 10 + int(c)
            else:
                curstr += c

        return curstr
