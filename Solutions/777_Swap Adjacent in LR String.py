"""
Keys:
- The hardest part of this question is to interpret the replacing rule into a code logic.
- Hint: Think of the L and R's as people on a horizontal line, where X is a space. The people
        can't cross each other, and also you can't go from XRX to RXX.

Complexity:
Time: O(n)
Space: O(n)
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace("X", "") != end.replace("X", ""):
            return False

        startl, startr, endl, endr = [], [], [], []

        for i, c in enumerate(start):
            if c == "L":
                startl.append(i)
            elif c == "R":
                startr.append(i)

        for i, c in enumerate(end):
            if c == "L":
                endl.append(i)
            elif c == "R":
                endr.append(i)

        for i, j in zip(startl, endl):
            if i < j:
                return False

        for i, j in zip(startr, endr):
            if i > j:
                return False

        return True
