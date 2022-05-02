"""
Keys:
- Random Pick problem. Not familiar with this type of questions. Need more practice.


Complexity:
time: O(n)
space: O(n)
"""


class Solution:

    def __init__(self, w: List[int]):
        self.boundaries = []
        totalWeight = 0
        for weight in w:
            totalWeight += weight
            self.boundaries.append(totalWeight)

    def pickIndex(self) -> int:
        num = random.random() * self.boundaries[-1]
        for i, boundary in enumerate(self.boundaries):
            if boundary > num:
                return i
