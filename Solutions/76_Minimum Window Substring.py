"""
Keys:
- use collections.Counter and a variable `counter` to simplify the solution.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        required = collections.Counter(t)
        counter = len(t)
        minl = float('inf')
        mins = ""

        for r in range(len(s)):
            if s[r] not in required:
                continue
            required[s[r]] -= 1
            if required[s[r]] >= 0:
                counter -= 1
            while counter == 0:
                if s[l] in required:
                    required[s[l]] += 1
                    if required[s[l]] > 0:
                        counter += 1
                        if r - l + 1 < minl:
                            minl = r - l + 1
                            mins = s[l: r+1]
                l += 1

        return mins
