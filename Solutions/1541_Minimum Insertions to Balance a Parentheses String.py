"""

"""


class Solution:
    def minInsertions(self, s: str) -> int:
        result = 0
        lst = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                lst.append(s[i])
                i += 1
            else:
                if i < len(s)-1 and s[i+1] == ")":
                    lst.append("))")
                    i += 2
                else:
                    result += 1
                    lst.append("))")
                    i += 1
        left = 0
        for c in lst:
            if c == "(":
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    result += 1
        result += 2 * left

        return result
