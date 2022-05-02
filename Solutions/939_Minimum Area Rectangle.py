"""
Keys:
- The set used in this solution is the trick for this question. It makes sure that we count each potential rectangular
  only once, which greatly optimizes the brute force.

Complexity:
Time: O(n^2)
Space: O(n)
"""


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        pointSet = set()
        mins = float('inf')

        for x, y in points:
            for x0, y0 in pointSet:
                if x == x0 or y == y0:
                    continue
                if (x0, y) in pointSet and (x, y0) in pointSet:
                    mins = min(mins, abs(x-x0) * abs(y-y0))
            pointSet.add((x, y))

        return mins if mins != float('inf') else 0
