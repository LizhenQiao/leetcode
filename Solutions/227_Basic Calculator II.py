"""
Keys:
- Most fundamental one of the Calculator questions.
- Key of solving this question is to use a variable to record last previous operator so that we could perform a calculation
  when we saw a operator. The reason of doing so is that only at the time we see next operator, we could get all the information
  of the previous operation. (Especially the second number in a complete form)
- According to the key stated above, we have a detailed trick here to make the code clean. Initialize `sign` as "+" and traverse
  (s + "+") to make sure that our first and last operations would be calculated in our mainstream iterations.  

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
                continue
            if c in "+-*/":
                if sign is "+":
                    stack.append(tmpnum)
                elif sign is "-":
                    stack.append(-tmpnum)
                elif sign is "*":
                    popnum = stack.pop()
                    stack.append(popnum * tmpnum)
                else:
                    popnum = stack.pop()
                    stack.append(int(popnum / tmpnum))
                sign = c
                tmpnum = 0

        return sum(stack)
