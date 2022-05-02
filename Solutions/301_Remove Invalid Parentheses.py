"""
Keys:
- Firstly, we figure out how many left parentheses and right parentheses we need to delete.
- Then we perform a normal recursion with backtracking to enumerate every possible sequences(After delete certain number
  of parentheses.)
- Finally, filter out the valid ones.

Complexity:
Time: Better than O(2^n) except for extreme cases.
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = len(s)
        result = []
        output = []
        left = right = 0

        for c in s:
            if c == ")":
                if not left:
                    right += 1
                else:
                    left -= 1
            elif c == "(":
                left += 1

        def dfs(index, s0, left, right):
            if index == l and left == 0 and right == 0:
                result.append(s0[:])
            if index == l:
                return None
            if left < 0 or right < 0:
                return None
            dfs(index+1, s0 + s[index], left, right)
            if s[index] == "(":
                dfs(index+1, s0, left-1, right)
            elif s[index] == ")":
                dfs(index+1, s0, left, right-1)

        dfs(0, "", left, right)
        for s1 in set(result):
            counter = 0
            signal = True
            for c in s1:
                if c == "(":
                    counter += 1
                elif c == ")":
                    counter -= 1
                if counter < 0:
                    signal = False
                    break

            if signal:
                output.append(s1[:])

        return output
