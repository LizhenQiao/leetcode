"""
Keys:
- The idea is in each iteration, firstly get end index, then get start index of a minimum window subsequence.
- The function to check if two strings match each other is a typical function to understand.

Complexity:
Time: O(n^2)
Space: O(1)
"""


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:

        def getEnd(i):
            j = 0
            while i < len(s1):
                if s1[i] == s2[j]:
                    j += 1
                i += 1
                if j == len(s2):
                    break
            return i - 1 if j == len(s2) else -1

        def getStart(i):
            j = len(s2) - 1
            while i >= 0:
                if s1[i] == s2[j]:
                    j -= 1
                i -= 1
                if j == -1:
                    break
            return i + 1

        minl = float('inf')
        mins = ""
        i = 0
        while i < len(s1):
            end = getEnd(i)
            if end == -1:
                break
            start = getStart(end)
            if end - start + 1 < minl:
                minl = end - start + 1
                mins = s1[start: end + 1]
            i = start + 1

        return mins
